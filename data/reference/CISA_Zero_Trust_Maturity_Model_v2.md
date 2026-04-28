# CISA Zero Trust Maturity Model v2.0 — Reference Guide
## Reference Guide for RLTech LLC

**Source:** Cybersecurity and Infrastructure Security Agency (CISA)
**Title:** Zero Trust Maturity Model, Version 2.0
**Published:** April 2023
**URL:** cisa.gov/zero-trust-maturity-model

---

## Purpose

The CISA Zero Trust Maturity Model (ZTMM) provides agencies with a roadmap and reference architecture to achieve an optimal Zero Trust environment over time. It complements NIST SP 800-207 by operationalizing Zero Trust across five pillars with specific maturity stages.

RLTech LLC uses the ZTMM as the scoring framework for Zero Trust Identity Readiness Assessments and as the basis for Zero Trust roadmaps delivered to federal clients.

---

## Five Pillars of Zero Trust (CISA ZTMM)

The ZTMM organizes Zero Trust capabilities into five pillars:

1. **Identity** — Authenticating and authorizing identity attributes for all users (federal and non-federal), non-person entities (NPEs), and devices acting on behalf of users
2. **Devices** — Hardware assets that access enterprise resources, including government-furnished equipment (GFE), BYOD, and IoT/OT
3. **Networks** — All internal and external network segments, including cloud and on-premises
4. **Applications & Workloads** — All software services, including on-prem apps, cloud-hosted, SaaS, and container workloads
5. **Data** — All structured and unstructured data, both in transit and at rest

**RLTech's specialization is the Identity pillar** — this is the first and foundational pillar for ZT adoption, and the one most directly addressed through Microsoft Entra ID, PIM, Conditional Access, and Identity Governance.

---

## Three Cross-Cutting Capabilities

In addition to the five pillars, the ZTMM defines three cross-cutting capabilities that span all pillars:

1. **Visibility and Analytics** — Collection and use of data about all components of the environment to drive access decisions and detect anomalies
2. **Automation and Orchestration** — Automated responses, policy enforcement, and workflow triggers based on real-time data
3. **Governance** — Policy management, risk management, and compliance oversight across all pillars

---

## Four Maturity Stages

Each pillar is assessed across four maturity stages:

| Stage | Description |
|---|---|
| **Traditional** | Manual configurations, siloed, reactive. Static policies. Limited visibility. Consistent with legacy perimeter-based security. |
| **Initial** | Some automation beginning. Cross-pillar integration starting. Basic attribute-based access control. Phishing-resistant MFA deployed for some users. |
| **Advanced** | Mostly automated. Dynamic policies based on real-time risk signals. Cross-pillar integration in place. Risk-based access decisions. |
| **Optimal** | Fully automated. Continuous validation. AI/ML-driven dynamic policy. Full lifecycle management. Self-healing capabilities. Continuous monitoring across all pillars. |

---

## Identity Pillar Detail (Most Relevant to RLTech)

The Identity pillar is CISA's recommended starting point for ZT adoption and directly maps to RLTech's service offerings.

### Identity Pillar Capabilities

**1. Identity Stores**
Comprehensive, centralized identity stores for all users (federal and contractor) and non-person entities (NPEs — service accounts, bots, automated pipelines).

| Stage | Identity Stores |
|---|---|
| Traditional | Siloed identity stores; manual account management; limited enterprise visibility |
| Initial | Partially centralized; automated provisioning beginning; some NPE inventory |
| Advanced | Centralized identity platform; automated lifecycle management (joiner/mover/leaver); NPE governance |
| Optimal | Single authoritative identity source; continuous lifecycle automation; complete NPE governance with just-in-time credentials |

**2. Risk Assessments**
Dynamic, real-time risk assessment applied to every access request.

| Stage | Risk Assessments |
|---|---|
| Traditional | Static risk assessments; infrequent reviews |
| Initial | Periodic risk scoring; some integration of threat intelligence |
| Advanced | Dynamic risk scores integrated into access decisions; identity risk signals from UEBA/SIEM |
| Optimal | Fully automated, continuous risk scoring; ML-driven anomaly detection; risk-adaptive authentication |

**3. Usable Credentials and Authentication**
Strong, phishing-resistant authentication for all users.

| Stage | Authentication |
|---|---|
| Traditional | Password-based; MFA partial or missing; PIV underutilized |
| Initial | MFA deployed for most users; PIV enforced for privileged users; password policies strengthened |
| Advanced | Phishing-resistant MFA (FIDO2 / PIV) enforced for all users; passwordless adoption underway |
| Optimal | Phishing-resistant MFA for all users and NPEs; passwordless authentication predominant; continuous authentication signals |

**4. Identity Federation and Provisioning**
Cross-organization identity federation and automated provisioning/de-provisioning.

| Stage | Federation and Provisioning |
|---|---|
| Traditional | Manual provisioning; minimal federation; contractor access is an afterthought |
| Initial | Partial federation; automated provisioning for most users |
| Advanced | Enterprise-wide federation; lifecycle automation for all users including contractors and NPEs |
| Optimal | Full automated lifecycle including cross-agency federation; real-time de-provisioning on separation |

**5. Access Management**
Attribute-based, risk-informed access control applied dynamically.

| Stage | Access Management |
|---|---|
| Traditional | Role-based access with static policies; minimal least-privilege enforcement |
| Initial | Some attribute-based access control (ABAC); privileged access separation beginning |
| Advanced | Dynamic ABAC; JIT privileged access (PIM); access reviews enforced; Conditional Access policies active |
| Optimal | Fully automated, dynamic access control; continuous access evaluation; JIT access for all privileged roles; automated access review and revocation |

---

## Devices Pillar Summary

| Capability | Traditional → Optimal |
|---|---|
| Asset inventory | Manual and incomplete → Real-time, automated, comprehensive |
| Device compliance | No enforcement → Device risk factored into every access decision |
| Endpoint detection | Perimeter-only → EDR deployed on all endpoints; signals integrated into access decisions |
| BYOD | No governance → Managed access policies for BYOD; containerized access where appropriate |

---

## Networks Pillar Summary

| Capability | Traditional → Optimal |
|---|---|
| Network segmentation | Flat network / coarse perimeters → Micro-segmentation per resource |
| Encryption | Partial → All traffic encrypted in transit (TLS 1.2+/1.3) |
| DNS security | Unprotected → Encrypted DNS (DoH/DoT); DNS monitoring |
| Traffic filtering | Perimeter firewall → Inline traffic inspection; application-layer filtering |

---

## OMB M-22-09 Alignment with CISA ZTMM

The CISA ZTMM v2.0 was developed to support federal agencies in meeting OMB M-22-09 requirements. Key alignments:

| OMB M-22-09 Requirement | CISA ZTMM Pillar | Target Stage |
|---|---|---|
| Phishing-resistant MFA for all staff | Identity | Advanced |
| PIV / CAC enforcement | Identity | Advanced |
| Privileged access management | Identity | Advanced |
| Device inventory and management | Devices | Advanced |
| Encrypted DNS | Networks | Advanced |
| Enforced HTTPS | Networks | Advanced |
| Application authorization | Applications & Workloads | Advanced |
| Data categorization | Data | Initial → Advanced |

---

## How RLTech Uses the CISA ZTMM

**Zero Trust Identity Readiness Assessment ($7,500 fixed-price):**
- Scores the client's Identity pillar across all five capabilities (Identity Stores, Risk Assessments, Authentication, Federation, Access Management)
- Assigns a maturity stage (Traditional / Initial / Advanced / Optimal) for each capability
- Identifies gaps between current state and OMB M-22-09 requirements
- Produces a prioritized roadmap of specific implementation steps

**Scoring approach:**
RLTech uses the CISA ZTMM scoring rubric to assign a current-state maturity level for each capability area. The deliverable includes a scored matrix, findings narrative, and a stage-by-stage roadmap showing exactly which controls to implement in which order.

---

## Useful ZTMM References for Proposals

- The CISA ZTMM is the **authoritative maturity model** for federal civilian Zero Trust implementation
- Citing CISA ZTMM and NIST SP 800-207 in proposals demonstrates technical credibility with federal contracting officers
- OMB M-22-09 requires agencies to demonstrate progress toward "Advanced" maturity across all five pillars by FY 2024
- Most agencies assessed by GAO and CISA OIG in 2023–2024 were at Traditional or Initial maturity — there is significant unmet need

---

*This reference document summarizes the CISA Zero Trust Maturity Model v2.0 (April 2023) for use by RLTech LLC consultants and Dominick Skelton. Always verify against the current published version at cisa.gov.*
