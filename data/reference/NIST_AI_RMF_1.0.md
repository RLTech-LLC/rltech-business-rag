# NIST AI Risk Management Framework (AI RMF 1.0) — Reference Guide
## Reference Guide for RLTech LLC

**Source:** National Institute of Standards and Technology (NIST)
**Title:** Artificial Intelligence Risk Management Framework (AI RMF 1.0)
**Published:** January 2023
**Document:** NIST AI 100-1
**URL:** nist.gov/artificial-intelligence

---

## Purpose and Scope

The NIST AI RMF is a voluntary framework to help organizations manage risks to individuals, organizations, and society from AI systems throughout their lifecycle. It is designed to be:

- **Voluntary** — Not mandatory for private organizations, but required or referenced by federal agency procurement in some cases
- **Risk-based** — Focuses on identifying, measuring, and managing AI-related risks
- **Flexible** — Applicable to any organization, sector, or AI application type
- **Iterative** — AI risk management is a continuous process, not a one-time assessment

The AI RMF is relevant to RLTech because:
1. Federal agencies deploying AI systems are required to consider NIST AI RMF alignment (OMB M-24-10, EO 14110 on AI)
2. RLTech's AI Workload Identity Security and AI Security Readiness Review services are explicitly aligned to the NIST AI RMF
3. As AI is deployed more broadly in federal environments, IAM/security professionals need to understand how identity controls fit into AI governance frameworks

---

## Core Structure: Two Parts

### Part 1 — Framing Risk
Describes the nature of AI risk, the characteristics of trustworthy AI, and the intended audience.

### Part 2 — Core and Profiles
Defines the AI RMF Core (four functions) and how organizations can build Profiles tailored to their context.

---

## Trustworthy AI Characteristics (Part 1)

NIST identifies seven characteristics of trustworthy AI systems:

1. **Accountable and Transparent** — The organization understands and can explain how the AI works and who is responsible for its decisions
2. **Explainable and Interpretable** — The AI's outputs can be understood and traced to their causes
3. **Fair with Harmful Bias Managed** — The AI treats users equitably and bias in data or design is identified and managed
4. **Privacy Enhanced** — The AI is designed to minimize privacy risks and comply with applicable privacy requirements
5. **Reliable and Resilient** — The AI performs consistently under expected and unexpected conditions
6. **Safe** — The AI does not cause harm to people, property, or the environment
7. **Secure and Cyber-Resilient** — **The AI is protected against unauthorized access, manipulation, and attacks** — this is the characteristic directly addressed by IAM and cybersecurity controls

---

## AI RMF Core: Four Functions

The AI RMF Core is organized into four functions. Think of these as the lifecycle of AI risk management — similar to how NIST CSF has Identify / Protect / Detect / Respond / Recover.

### GOVERN

**What it is:** Organizational policies, processes, and structures that establish accountability for AI risk management across the enterprise.

**Why it matters for IAM/security:**
- Who is authorized to deploy an AI system? Who reviews access to AI training data and model outputs?
- What policy exists for approving AI workloads? Is there an AI governance board?
- How are AI systems inventoried and tracked as organizational assets?
- What access controls govern who can query, modify, or retrain an AI model?

**Key Govern categories:**
- G1: Policies, processes, procedures, and practices are in place for AI risk management
- G2: Accountability for AI risk management is defined and documented
- G3: Workforce has sufficient AI risk competency
- G4: Organizational culture supports AI risk transparency
- G5: AI risk management policies are reviewed and updated regularly
- G6: Policies/procedures address AI risk across the supply chain (third-party AI)

### MAP

**What it is:** The process of identifying and categorizing AI risks in context — who the AI affects, what the risk scenarios are, and how risks compare to benefits.

**Why it matters for IAM/security:**
- Mapping includes identifying what data the AI accesses, what credentials it uses, and what systems it can affect
- Non-human identities (service accounts, managed identities used by AI pipelines) must be mapped as part of the risk context
- Who can submit prompts to the AI? Who has access to the AI's responses and logs?

**Key Map categories:**
- M1: Context is established for the AI deployment (stakeholders, use case, data, environment)
- M2: Scientific and technical understanding of AI risks is applied
- M3: AI risks are categorized (harms to people, organizations, society, environment)
- M4: AI risks are prioritized based on likelihood and severity
- M5: Organizational risk tolerance is applied to AI risk assessment outputs

### MEASURE

**What it is:** Quantitative and qualitative methods to assess AI risk, including testing, evaluation, and monitoring.

**Why it matters for IAM/security:**
- Penetration testing of AI systems — can they be manipulated by unauthorized users?
- Adversarial testing (prompt injection, data poisoning, model extraction)
- Monitoring AI system behavior for anomalies (akin to UEBA for human users)
- Access log analysis: who is querying the AI, with what frequency, and for what purpose?

**Key Measure categories:**
- M1: AI risk measurement approaches are identified and applied
- M2: AI systems are tested for harmful bias, security, and reliability
- M3: AI system risk metrics are tracked over time
- M4: Results of AI risk measurement are used to improve the AI system

### MANAGE

**What it is:** Actions taken to address AI risks — including accepting, avoiding, mitigating, or transferring risk.

**Why it matters for IAM/security:**
- Incident response for AI systems — if an AI is manipulated or its access credentials compromised, what is the response plan?
- Remediation: patching AI models, revoking compromised credentials, isolating affected workloads
- Risk acceptance documentation for AI systems with residual risk

**Key Manage categories:**
- M1: Risks to AI systems are addressed using appropriate risk treatment strategies
- M2: Treatment of AI risks is documented and tracked
- M3: Responses to AI incidents are implemented and reviewed
- M4: Residual risks are communicated to appropriate stakeholders

---

## AI RMF Profiles

A **Profile** is the set of AI RMF outcomes an organization chooses to prioritize based on their context, risk tolerance, and stakeholder requirements. There is no single "correct" profile — organizations develop profiles tailored to:

- The type of AI (generative AI, decision-support AI, autonomous systems)
- The sector (federal government, healthcare, financial services)
- The application (hiring, fraud detection, medical diagnosis)
- The risk appetite of the organization

NIST has published a **Generative AI Profile** (NIST AI 600-1) specifically for large language models and generative AI systems.

---

## AI Identity and Access Management Risks (IAM Lens)

RLTech's AI security services focus specifically on the identity and access control risks associated with AI workloads. Key risk areas:

### 1. Over-Privileged AI Service Identities
AI systems that use service principals or managed identities with excessive permissions. An AI pipeline with Owner-level access to an Azure subscription is a critical risk — if the service identity is compromised or the AI model is manipulated, the blast radius is catastrophic.

**Mitigation:** Principle of least privilege for all AI service identities; use Managed Identities where possible (no credential to steal); scope permissions to specific resources; implement PIM for elevated access.

### 2. Uncontrolled Access to AI Systems
Who can query the AI system? Who can access training data? Who can retrain or fine-tune the model?

**Mitigation:** Role-based access control (RBAC) on AI endpoints; Conditional Access for AI portals and APIs; audit logging of all AI interactions.

### 3. Credential Leakage in AI Pipelines
AI training pipelines, RAG systems, and automated workflows often handle API keys, database credentials, and access tokens. These are frequently hardcoded in configuration files, notebooks, or CI/CD pipelines.

**Mitigation:** Azure Key Vault for all secrets used by AI pipelines; Managed Identities instead of client secrets; secret scanning in CI/CD; rotation policies for all AI service credentials.

### 4. Prompt Injection and Data Exfiltration
A malicious user could inject prompts into a RAG or generative AI system that cause it to retrieve sensitive documents it should not share.

**Mitigation:** Document-level access controls on the knowledge base (Azure AI Search security trimming); Conditional Access on AI portal; audit logging; output filtering.

### 5. Non-Human Identity Governance
AI systems create large numbers of non-human identities — service principals for each pipeline, managed identities for each Azure resource, app registrations for each integration. These accumulate over time without governance.

**Mitigation:** Regular NPE inventory and access reviews; Entra Workload ID lifecycle governance; automated cleanup of unused app registrations.

---

## Federal AI Requirements (EO 14110 and OMB M-24-10)

**Executive Order 14110** (October 2023, Safe, Secure, and Trustworthy AI) directed:
- Federal agencies to use AI safely and responsibly
- NIST to develop AI safety standards (leading to NIST AI 100-1 and 600-1)
- AI developers to report safety test results to the government
- Agencies to appoint Chief AI Officers (CAIOs)

**OMB M-24-10** (March 2024, Advancing Governance, Innovation, and Risk Management for Agency Use of Artificial Intelligence) directed:
- All federal agencies to designate a Chief AI Officer
- Agencies to complete AI use case inventories
- Agencies to implement minimum risk practices for "rights-impacting" and "safety-impacting" AI uses
- AI risk management practices must align with NIST AI RMF

---

## How RLTech Uses the NIST AI RMF

**AI Security Readiness Review:**
RLTech's AI Security Readiness Review scores a client's AI deployment against the NIST AI RMF GOVERN and MEASURE functions, with specific focus on the "Secure and Cyber-Resilient" trustworthy AI characteristic. Deliverables include:

- NIST AI RMF scorecard (Govern / Map / Measure / Manage)
- Identity-layer risk findings for deployed AI systems (over-privileged identities, uncontrolled access, credential management)
- Recommended controls mapped to both AI RMF and NIST Cybersecurity Framework
- Remediation roadmap

**AI Workload Identity Scan:**
Specifically addresses the IAM dimension of AI risk — inventories all service principals, managed identities, and app registrations used by AI workloads; identifies over-privileged identities; recommends governance controls.

---

## Useful Definitions from NIST AI RMF

| Term | NIST AI RMF Definition |
|---|---|
| AI System | An engineered or machine-based system that can, for a given set of objectives, generate outputs such as predictions, recommendations, decisions, or content that influence real or virtual environments |
| AI Risk | The composite measure of an event's probability of occurring and the magnitude or degree of the consequence of the corresponding event |
| Trustworthy AI | AI systems that are accountable, explainable, interpretable, privacy-enhanced, reliable, resilient, safe, secure, and cyber-resilient |
| AI Actor | Any organization or individual that plays a role in the AI lifecycle (developer, operator, user, evaluator) |
| AI Lifecycle | All stages of an AI system from conception to decommission: design, development, training, testing, deployment, operation, monitoring, and retirement |

---

*This reference document summarizes NIST AI RMF 1.0 (January 2023, NIST AI 100-1) for use by RLTech LLC consultants and Dominick Skelton. Always verify against the current published version at nist.gov/artificial-intelligence.*
