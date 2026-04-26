# RLTech Business RAG — Deployment Guide

End-to-end instructions for deploying and operating the production RAG system.

---

## Architecture

| Service | Purpose | SKU |
|---|---|---|
| **Azure OpenAI** | Chat (gpt-4.1-mini) + embeddings (text-embedding-3-large) | S0 |
| **Azure AI Search** | Hybrid full-text + vector retrieval with semantic ranking | Basic |
| **Azure Blob Storage** | Document storage and ingestion staging | Standard\_LRS |
| **Azure Container Apps** | Serverless container hosting for the web application | Consumption |
| **Azure Container Registry** | Container image storage and ACR Build | Basic |
| **Azure Document Intelligence** | PDF / DOCX / image layout analysis and extraction | S0 |
| **Azure Application Insights** | Distributed tracing, performance monitoring | — |

All services authenticate to each other using **Managed Identity** (keyless RBAC). No API keys are stored in application code or CI pipelines.

---

## Prerequisites

### 1 — Azure subscription

- An Azure subscription where you have **Contributor** or **Owner** at the subscription scope (required for the subscription-scoped Bicep deployment that creates resource groups and assigns RBAC roles).

### 2 — Service principal with OIDC federated credentials

Create a service principal and configure GitHub OIDC federated identity so that GitHub Actions can authenticate to Azure without storing a client secret.

```bash
# Create the app registration
az ad app create --display-name "rltech-rag-deployer"

APP_ID=$(az ad app list --display-name "rltech-rag-deployer" --query "[0].appId" -o tsv)
SP_ID=$(az ad sp create --id "$APP_ID" --query id -o tsv)

# Assign Contributor at subscription scope
az role assignment create \
  --assignee "$SP_ID" \
  --role Contributor \
  --scope "/subscriptions/$(az account show --query id -o tsv)"
```

Then add a **federated credential** in the Azure portal (or via CLI) scoped to:

- Issuer: `https://token.actions.githubusercontent.com`
- Subject: `repo:RLTech-LLC/rltech-business-rag:environment:prod`
- Audience: `api://AzureADTokenExchange`

Microsoft reference: [Connect GitHub Actions to Azure with OIDC](https://learn.microsoft.com/azure/developer/github/connect-from-azure)

### 3 — GitHub repository configuration

#### Secrets (Settings → Secrets and variables → Actions → Secrets)

| Secret | Value |
|---|---|
| `AZURE_CLIENT_ID` | App registration client ID (from step 2) |
| `AZURE_TENANT_ID` | Azure AD tenant ID |
| `AZURE_SUBSCRIPTION_ID` | Azure subscription ID |

#### Variables (Settings → Secrets and variables → Actions → Variables)

| Variable | Example value | Description |
|---|---|---|
| `AZURE_ENV_NAME` | `rltech-rag-prod` | Short environment name — used as the base for all resource names. Use lowercase letters, numbers, and hyphens only. |
| `AZURE_PRINCIPAL_ID` | `<object-id>` | Object ID of the service principal created in step 2. Run `az ad sp show --id $APP_ID --query id -o tsv` to retrieve it. |

#### GitHub Environment

Create a GitHub environment named **`prod`** (Settings → Environments) and add any required protection rules (e.g., required reviewers).

---

## Deployment Steps

### Step 1 — Provision infrastructure

Run the **Provision Infrastructure** workflow manually from the Actions tab:

1. Navigate to **Actions → Provision Infrastructure → Run workflow**.
2. Select your region. Use a region that supports all services. Recommended: `eastus2`.
3. Select your OpenAI region. Recommended: `eastus2` (wide model availability).
4. Select your Document Intelligence region. Recommended: `eastus`.
5. Click **Run workflow**.

The workflow runs `az deployment sub create` against `infra/main.bicep`. It creates:

- A resource group `rg-<AZURE_ENV_NAME>`
- All Azure services listed in the architecture table above
- RBAC role assignments for the application's managed identity and the deploying principal

**Duration:** ~10–15 minutes.

> **Idempotent:** The workflow uses a fixed deployment name (`rltech-rag-infra`) so re-running it updates existing resources rather than duplicating them.

### Step 2 — Deploy the application

Run the **Deploy Application** workflow manually, or it triggers automatically on `push` to `main` when files under `app/` change:

1. Navigate to **Actions → Deploy Application → Run workflow**.
2. Click **Run workflow**.

The workflow:

1. Builds the React frontend (`npm ci && npm run build`) — output goes to `app/backend/static/`.
2. Builds the Docker image in ACR Build (`az acr build`) — no local Docker daemon needed.
3. Updates the Container App to use the new image (`az containerapp update`).

**Duration:** ~5–8 minutes.

### Step 3 — Add your business documents

Place your documents in the `data/` directory (or a subdirectory), commit and push them, then run the **Ingest Business Documents** workflow:

```text
data/
├── contracts/
│   ├── vendor-agreement-2024.pdf
│   └── software-license.pdf
├── policies/
│   ├── information-security-policy.pdf
│   └── data-retention-policy.docx
└── compliance/
    └── soc2-report.pdf
```

Supported formats: `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`, `.md`, `.txt`, `.csv`, `.json`, `.png`, `.jpg`

#### Run ingestion

1. Navigate to **Actions → Ingest Business Documents → Run workflow**.
2. Set **data path** (e.g., `data/` for all documents, or `data/contracts/` for a subset).
3. Click **Run workflow**.

The workflow runs `prepdocs.py`, which:

- Uploads raw documents to Azure Blob Storage.
- Extracts text and structure using Azure Document Intelligence.
- Splits content into overlapping chunks.
- Generates vector embeddings via Azure OpenAI (`text-embedding-3-large`, 3072 dimensions).
- Indexes chunks in Azure AI Search (hybrid text + vector index).

**Duration:** varies by document size. Expect ~1–2 minutes per PDF page for Document Intelligence parsing.

> **Re-ingestion:** To replace all documents, check **Remove all first** before running the workflow.

---

## Using the System

Once all three steps are complete, open the application URL shown in the **Provision Infrastructure** step summary (or run the command below):

```bash
az containerapp show \
  --resource-group "rg-<AZURE_ENV_NAME>" \
  --name <container-app-name> \
  --query "properties.configuration.ingress.fqdn" \
  --output tsv
```

The web interface provides:

- **Chat** — ask natural-language questions over your business documents.
- **Citations** — every answer cites the source document and page.
- **Developer settings** — tune retrieval parameters (top-K, semantic ranking, vector weights).

---

## Ongoing Operations

### Adding new documents

1. Place new files in `data/` (or a subdirectory).
2. Commit and push the files.
3. Run **Ingest Business Documents** workflow targeting the new subdirectory.

### Updating the application

Push changes to `app/` on `main`. The **Deploy Application** workflow triggers automatically.

### Re-provisioning infrastructure

Re-run **Provision Infrastructure** at any time. Existing data and deployed containers are preserved (the Bicep deployment is idempotent).

### Tearing down

```bash
az group delete --name "rg-<AZURE_ENV_NAME>" --yes --no-wait
```

If you want to re-provision after teardown, set **Restore soft-deleted Cognitive Services** to `true` on the next workflow run to reuse soft-deleted accounts (avoids the 90-day purge wait).

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Infra workflow fails at Bicep deployment | Service principal lacks Contributor | Re-check role assignment scope |
| `az acr build` fails | SP lacks `AcrImageSigner` or Contributor on ACR | Add `AcrImageSigner` role on the registry |
| Ingest fails: `AZURE_SEARCH_SERVICE not set` | Infra not deployed, or outputs not readable | Run Provision Infrastructure first |
| Chat returns "no documents found" | Ingestion not run, or wrong data path | Run Ingest Documents workflow |
| App shows 502 / timeout | Container App has 0 replicas (cold start) | Wait 30s and retry; or set `containerMinReplicas=1` in Bicep |

---

## Key Microsoft Documentation

- [Azure OpenAI RAG reference architecture](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
- [Azure AI Search hybrid retrieval](https://learn.microsoft.com/azure/search/hybrid-search-overview)
- [Azure Container Apps Consumption profile](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
- [Azure Document Intelligence layout model](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-layout)
- [GitHub Actions OIDC authentication to Azure](https://learn.microsoft.com/azure/developer/github/connect-from-azure)
- [Bicep subscription-scope deployment](https://learn.microsoft.com/azure/azure-resource-manager/bicep/deploy-to-subscription)
- [ACR Build Tasks](https://learn.microsoft.com/azure/container-registry/container-registry-tutorial-quick-task)
