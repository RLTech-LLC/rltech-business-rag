# RLTech Business RAG — Project Roadmap

**Last updated:** 2026-04-28
**Owner:** Dominick Skelton, RLTech LLC
**Purpose:** Central reference document for ongoing development of the RLTech business knowledge base. Paste this into every new AI coding session to maintain continuity.

---

## What This System Does

A ChatGPT-like assistant grounded in RLTech's own business documents — services catalog, rate sheet, capability statement, proposal templates, and compliance references. Users ask natural-language questions and get cited, factual answers drawn from those documents. Built on the Azure RAG stack: Azure OpenAI + Azure AI Search + Azure Container Apps.

---

## Current State (as of 2026-04-28)

### Deployed infrastructure
- Azure Container Apps (Consumption) hosting the Quart/Python backend
- Azure AI Search (Basic SKU, `gptkbindex`) with hybrid text + vector retrieval
- Azure OpenAI: `gpt-4.1-mini` (chat) + `text-embedding-3-large` (3072-dim embeddings)
- Azure Document Intelligence (S0) for PDF/DOCX parsing
- Azure Blob Storage (Standard_LRS)
- Application Insights enabled
- GitHub Actions CI/CD: provision (`infra-deploy.yml`), deploy (`app-deploy.yml`), ingest (`ingest-documents.yml`)

### Knowledge base contents (`data/`)
| File | Type | Status |
|---|---|---|
| `RLTech_Capability_Statement.md` | Core capability doc | ✅ Clean |
| `RLTech_Services_Catalog.md` | Services + micro-purchase packages | ⚠️ Has `[X]` placeholder (line 85) |
| `RLTech_Rate_Sheet.md` | T&M rates, fixed-price, retainers | ✅ Clean |
| `RLTech_NDA_Template.md` | NDA template | ✅ Clean |
| `RLTech_SOW_Template.md` | Statement of Work template | ⚠️ Has `[X]` placeholder (line 135) |
| `RLTech_Teaming_Agreement_Template.md` | Teaming agreement template | ✅ Clean |
| PDFs (W-9, EIN, CAGE/SAM, operating agreement, etc.) | Corporate registrations | ⚠️ Sensitive — verify repo visibility |

### Evaluation baselines
Best configuration: **`gpt5chat-emb3l`** (gpt-5-chat + text-embedding-3-large)
- Groundedness: 96% | Relevance: 90% | Latency: 2.9s

> ⚠️ **IMPORTANT:** The current `evals/ground_truth.jsonl` contains 50 questions about
> Contoso/Northwind Health benefits (leftover from the Microsoft sample template).
> All eval scores are currently meaningless for RLTech's actual knowledge base.
> This must be replaced before trusting any eval run.

---

## Cross-Session Checklist

**Paste these checks into every new AI coding session before making changes:**

- [ ] Read this file (`docs/ROADMAP.md`) to understand current phase
- [ ] Verify `evals/ground_truth.jsonl` reflects RLTech content (not Northwind/Contoso) before running any eval
- [ ] Confirm repo visibility settings before committing new sensitive files to `data/`
- [ ] Run `source .venv/bin/activate && pytest tests/` and confirm ≥ 90% coverage before any backend PR
- [ ] After any `data/` change, trigger the **Ingest Business Documents** GitHub Actions workflow
- [ ] After any infrastructure change (`infra/`), trigger the **Provision Infrastructure** workflow

---

## Phase 1 — Foundation ✅ Complete

- [x] Fork and adapt Microsoft `azure-search-openai-demo` template
- [x] Replace Zava/Contoso sample data with RLTech business documents
- [x] Configure GitHub Actions CI/CD (provision, deploy, ingest)
- [x] Multi-model evaluation harness in place (`evals/`)
- [x] Custom deployment guide (`docs/deployment-guide.md`)
- [x] OIDC federated credentials (no long-lived secrets in CI)

---

## Phase 2 — Knowledge Base Quality 🔴 Immediate Priority

### 2a. Fix eval ground truth
- [ ] Delete `evals/ground_truth.jsonl` Northwind/Contoso content
- [ ] Write 30–50 Q&A pairs grounded in RLTech documents, covering:
  - Rate inquiries ("what is the hourly rate for a Senior IAM Consultant?")
  - Service scope ("what is included in the Zero Trust Identity Readiness Report?")
  - Compliance framework references ("which frameworks does the IAM Assessment map to?")
  - NAICS/procurement questions ("which services are micro-purchase eligible?")
  - Template usage ("what fields need to be filled in the SOW template?")
- [ ] Run `evals/evaluate.py` with new ground truth to establish a real baseline
- [ ] Commit baseline results to `evals/results/rltech-baseline/`

### 2b. Fix the system prompt
- [ ] Edit `app/backend/approaches/prompts/chat_answer.system.jinja2`
  - Replace generic *"helps company employees with internal documents"* persona
  - Replace pharmacy/medication follow-up question examples (lines 27–29)
  - Tune for RLTech's IAM/government consulting context

### 2c. Fix knowledge base gaps
- [ ] Fill `[X]` placeholder in `data/RLTech_Services_Catalog.md` line 85 (retainer hours)
- [ ] Fill `[X]` placeholder in `data/RLTech_SOW_Template.md` line 135 (duration estimate)

### 2d. Add Microsoft reference documentation (see section below)

---

## Phase 3 — Production Hardening 🟡 Before Sharing the URL

- [ ] Enable authentication (`AZURE_USE_AUTHENTICATION=true`) — the rate sheet, W-9, and
      operating agreement are marked CONFIDENTIAL and must not be publicly accessible
- [ ] Upgrade storage SKU: `AZURE_STORAGE_SKU=Standard_ZRS` (zone-redundant)
- [ ] Upgrade AI Search: `AZURE_SEARCH_SERVICE_SKU=standard` + `AZURE_SEARCH_SEMANTIC_RANKER=standard`
      (free tier fails after 1,000 queries/month)
- [ ] Rename search index: set `AZURE_SEARCH_INDEX=rltech-biz-kb` (replace generic `gptkbindex`)
- [ ] Set `containerMinReplicas=1` in Bicep to eliminate cold-start delays

---

## Phase 4 — Scaling the Knowledge Base 🟢 Ongoing

### 4a. Add compliance and certification reference docs
See **Microsoft Docs Strategy** section below for how to do this.

Priority documents to add:
| Document | Source | Format |
|---|---|---|
| SC-300 exam skills outline | Microsoft Learn (PDF download) | PDF |
| NIST SP 800-207 (Zero Trust Architecture) | csrc.nist.gov | PDF |
| NIST SP 800-63-3 (Digital Identity Guidelines) | csrc.nist.gov | PDF |
| CISA Zero Trust Maturity Model v2.0 | cisa.gov | PDF |
| OMB M-22-09 (Federal Zero Trust Strategy) | whitehouse.gov | PDF |
| Microsoft Entra ID documentation (key pages) | learn.microsoft.com | MD (crawled) |
| Microsoft Zero Trust deployment guide | learn.microsoft.com | MD (crawled) |
| CIS Microsoft 365 Foundations Benchmark | cisecurity.org (requires account) | PDF |

### 4b. Add business development content as it is created
- [ ] Past performance write-ups (as engagements complete)
- [ ] Case studies / sanitized client summaries
- [ ] Proposal sections / boilerplate paragraphs
- [ ] GSA MAS schedule content (when awarded)

### 4c. Add metadata fields to search index for IAM-domain filtering
- [ ] Add `compliance_framework` field (NIST, CISA, FedRAMP, CIS, OMB)
- [ ] Add `service_area` field (Assessment, Implementation, AI-Security, Staff-Aug)
- [ ] Add `document_type` field (rate_sheet, capability, template, registration, reference)
- [ ] Update `app/backend/prepdocslib/searchmanager.py` index schema
- [ ] Update ingestion pipeline to tag documents with these fields

---

## Phase 5 — Business Development Use Cases 🔵 Future

- [ ] "Generate SOW draft" guided prompt flow based on selected service package
- [ ] "Find the right micro-purchase package" guided Q&A
- [ ] "Write a capability section" prompt using RLTech's differentiators
- [ ] Evaluate SharePoint source integration (`USE_SHAREPOINT_SOURCE=true`) for
      live sync of documents stored in SharePoint/OneDrive
- [ ] Partner-facing access tier (different ACL from internal view)

---

## Microsoft Docs Strategy

### Short answer: **You download PDFs; I fetch targeted web pages — hybrid is best.**

#### Official government / NIST / CISA documents → **You download these**
These are static, authoritative PDFs that rarely change. Go get them directly:
- [NIST SP 800-207](https://doi.org/10.6028/NIST.SP.800-207) — Zero Trust Architecture
- [NIST SP 800-63-3](https://pages.nist.gov/800-63-3/) — Digital Identity (download the PDF)
- [CISA ZTMM v2.0](https://www.cisa.gov/zero-trust-maturity-model) — download from cisa.gov
- [OMB M-22-09](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf)

Put them in `data/compliance/` and trigger the Ingest workflow. These change rarely —
re-download when new versions are published (e.g., NIST SP 800-63-4 when finalized).

#### Microsoft Learn docs → **I fetch targeted pages for you**
I can use `web_fetch` to pull specific Microsoft Learn pages and save them as `.md`
files in `data/microsoft-docs/`. This is reliable for targeted, high-value pages.

Recommended approach:
1. Tell me which doc areas you want (e.g., "SC-300 study guide", "Entra Conditional Access")
2. I identify the canonical URLs and fetch the content
3. I save them into `data/microsoft-docs/<area>/` as markdown
4. You trigger the Ingest Documents workflow

Limitations:
- Microsoft Learn pages change regularly — plan to re-fetch quarterly
- Some pages are very long and may need to be split into sub-pages
- Interactive/lab content won't translate to useful RAG chunks

#### SC-300 specifically
The SC-300 exam skills outline PDF is the best single document to add.
Download from: https://learn.microsoft.com/en-us/credentials/certifications/exams/sc-300/
(scroll to "Skills measured" → "Download exam skills outline")

---

## Key File Reference

| File | What it does |
|---|---|
| `app/backend/approaches/prompts/chat_answer.system.jinja2` | System prompt — tune this for RLTech's context |
| `app/backend/approaches/prompts/query_rewrite.system.jinja2` | Query rewriting prompt |
| `app/backend/prepdocslib/searchmanager.py` | Search index schema — add metadata fields here |
| `evals/ground_truth.jsonl` | Eval Q&A — replace with RLTech questions |
| `evals/evaluate_config.json` | Eval run config (retrieval params) |
| `infra/main.parameters.json` | All azd environment variable defaults |
| `data/` | All knowledge base documents |
| `docs/deployment-guide.md` | Step-by-step deployment instructions |

---

## Known Issues (open)

| Issue | Severity | Phase |
|---|---|---|
| Eval ground truth is Northwind/Contoso content — all scores are wrong | 🔴 Critical | 2a |
| System prompt says "company employees / internal documents" — wrong persona | 🔴 High | 2b |
| `[X]` placeholders in Services Catalog and SOW Template | 🔴 High | 2c |
| Authentication disabled by default — confidential docs are publicly accessible | 🟡 Medium | 3 |
| Storage uses Standard_LRS (not zone-redundant) | 🟡 Medium | 3 |
| AI Search on free semantic ranker tier (1,000 query/month cap) | 🟡 Medium | 3 |
| Search index named `gptkbindex` (generic sample name) | 🟢 Low | 3 |
| W-9/EIN/operating agreement PDFs committed to repo — verify visibility | 🟡 Medium | 3 |
