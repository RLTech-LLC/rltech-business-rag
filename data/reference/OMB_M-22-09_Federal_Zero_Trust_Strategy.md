# OMB M-22-09 — Moving the U.S. Government Toward Zero Trust Cybersecurity Principles
## Reference Guide for RLTech LLC

**Source:** Office of Management and Budget (OMB)
**Memorandum:** M-22-09
**Title:** Moving the U.S. Government Toward Zero Trust Cybersecurity Principles
**Issued:** January 26, 2022
**Directed to:** Heads of Executive Departments and Agencies

---

## Purpose and Background

OMB M-22-09 directed all federal civilian executive branch (FCEB) agencies to meet specific Zero Trust security goals by the end of Fiscal Year 2024 (September 30, 2024). The memo implements requirements from Executive Order 14028 (Improving the Nation's Cybersecurity, May 2021) and the National Security Memorandum on Improving Cybersecurity for Critical Infrastructure Control Systems.

The memo adopts **CISA's Zero Trust Maturity Model** and **NIST SP 800-207** as the technical reference standards for federal ZT implementation.

---

## Federal Zero Trust Strategy: Five Pillars

M-22-09 is organized around five pillars, each with specific required actions for agencies:

### 1. Identity
### 2. Devices
### 3. Networks
### 4. Applications and Workloads
### 5. Data

---

## Pillar 1: Identity — Key Requirements

Identity is the first and highest-priority pillar in M-22-09. The memo states: *"Agency staff use enterprise-managed identities to access the applications they use in their work, and phishing-resistant multi-factor authentication (MFA) protects those personnel from sophisticated online attacks."*

### Required actions:

**1.1 Phishing-Resistant MFA for All Agency Staff**
- All agency personnel must use phishing-resistant MFA to access enterprise applications
- Phishing-resistant methods: PIV/CAC smart cards, FIDO2 security keys (WebAuthn), platform authenticators (Windows Hello for Business, Touch ID on managed devices)
- SMS-based OTP, authenticator app TOTP, and push notification MFA are **NOT** considered phishing-resistant under M-22-09
- Agencies may not count SMS/TOTP as meeting this requirement

**1.2 Enterprise-Managed Identities**
- All agency staff must access applications using enterprise-managed identities (no personal accounts for work systems)
- Single Sign-On (SSO) for all enterprise applications where technically feasible

**1.3 PIV / CAC Integration**
- Existing PIV (Personal Identity Verification) credentials must be the primary authentication method for most federal staff
- Agencies must enforce PIV login for all systems that support it
- For systems that cannot support PIV natively, FIDO2 / WebAuthn tokens are the approved phishing-resistant alternative

**1.4 Non-Person Entities (NPEs)**
- Agencies must inventory all non-person entities (service accounts, bots, automated pipelines, managed identities)
- NPEs must use short-lived credentials or tokens where possible; persistent credentials must be governed, rotated, and monitored
- Multi-factor authentication is not directly applicable to NPEs — the equivalent is certificate-based authentication, managed identity, or workload identity federation

**1.5 MFA for Contractors and Partners**
- Contractors and partners accessing agency systems must also use enterprise-managed identities with phishing-resistant MFA

### M-22-09 Identity Maturity Requirement Summary

| Requirement | Target (by end of FY2024) |
|---|---|
| Phishing-resistant MFA for all agency staff | Required |
| PIV enforcement for all PIV-capable systems | Required |
| SSO for all new applications | Required |
| NPE inventory | Required |
| Contractor MFA | Required |

---

## Pillar 2: Devices — Key Requirements

*"The Federal Government has a complete inventory of every device it operates and authorizes for Government use, and can prevent, detect, and respond to incidents on those devices."*

### Required actions:

- **Device inventory** — Agencies must maintain a comprehensive, up-to-date inventory of all government-furnished equipment (GFE)
- **Mobile Device Management (MDM)** — All GFE enrolled in MDM; agencies must be able to remotely wipe
- **Endpoint Detection and Response (EDR)** — EDR deployed on all Federal Civilian Executive Branch (FCEB) endpoints; logs sent to agency SOC and to CISA's CDM (Continuous Diagnostics and Mitigation) program
- **Device compliance integrated into access control** — Device health/compliance status must be a factor in access decisions (aligned to CISA ZTMM Device pillar Advanced stage)
- **BYOD governance** — Agencies must define clear policies for BYOD; personal devices accessing federal data must meet minimum security requirements

---

## Pillar 3: Networks — Key Requirements

*"Agencies encrypt all DNS requests and HTTP traffic within their environment, and they are working toward implementing a comprehensive micro-segmentation strategy."*

### Required actions:

- **Encrypted DNS (DNS-over-HTTPS / DNS-over-TLS)** — All agency DNS queries must be encrypted; DNS queries must be routed through an encrypted resolver
- **HTTPS enforcement** — All internal and external agency web traffic must use HTTPS (TLS 1.2 minimum; TLS 1.3 preferred); HTTP redirected to HTTPS
- **Email encryption and authentication** — DMARC enforcement for all agency email domains; DKIM and SPF required
- **Network segmentation (roadmap)** — Agencies must develop a plan for macro and micro-segmentation; full implementation is a longer-term goal beyond FY2024
- **Encrypted traffic inspection** — Agencies must have a plan for inspecting encrypted traffic flowing across network boundaries

---

## Pillar 4: Applications and Workloads — Key Requirements

*"Agencies treat all applications as internet-connected, routinely subject their applications to rigorous empirical testing, and welcome external vulnerability reports."*

### Required actions:

- **Applications treated as internet-connected** — Applications should be accessible via strong authentication regardless of network location; VPN is not a substitute for strong application-level authentication
- **Application vulnerability testing** — Agencies must conduct testing on all internet-facing applications; bug bounty programs encouraged
- **Immutable application logs** — All application access logs must be generated and stored in a form that cannot be altered; logs must be forwarded to a SIEM
- **Cloud application security (CASB)** — Agencies using SaaS applications must use a CASB to enforce access policy and DLP
- **Authorization** — All applications must enforce least-privilege authorization per user session; standing access to privileged functions must be minimized

---

## Pillar 5: Data — Key Requirements

*"Agencies are cataloging the data in their systems, establishing clear policies for how data should be handled, and implementing technical controls to enforce those policies."*

### Required actions:

- **Data categorization and inventory** — Agencies must categorize data at a minimum using the NIST information impact levels or agency-specific classification; sensitive data must be identified and inventoried
- **Data Loss Prevention (DLP)** — Agencies must deploy DLP solutions for sensitive data categories (CUI, PII, financial data)
- **Cloud Access Security Broker (CASB)** — Required for SaaS environments to enforce data access policies and detect exfiltration
- **Encryption at rest** — All federal data must be encrypted at rest; encryption keys must be managed by the agency (not the cloud provider)

---

## Agency Zero Trust Architecture Strategy Requirement

M-22-09 required each agency to develop and submit a Zero Trust Architecture Strategy to OMB and CISA within 60 days. The strategy must include:

1. An assessment of current state against the CISA ZTMM
2. A plan for achieving the required maturity goals by end of FY2024
3. Identification of gaps and resource needs
4. An agency-wide implementation roadmap

---

## What Counts as Phishing-Resistant MFA?

This is the most frequently misunderstood requirement in M-22-09. The memo is explicit:

**Phishing-Resistant (meets M-22-09):**
- PIV / CAC smart cards
- FIDO2 / WebAuthn security keys (YubiKey, etc.)
- Platform authenticators — Windows Hello for Business, Touch ID (on managed devices), Face ID (on managed devices)

**NOT Phishing-Resistant (does NOT meet M-22-09 for staff):**
- SMS / text message OTP
- Voice call OTP
- Time-based OTP (TOTP) apps (Google Authenticator, Microsoft Authenticator TOTP mode)
- Push notification MFA (Microsoft Authenticator push, Duo push) — NOTE: Microsoft Authenticator with Number Matching and Additional Context is a significant improvement but is still technically push-based; agencies should use FIDO2 or PIV to fully meet the requirement

---

## Definitions

| Term | M-22-09 Definition |
|---|---|
| Zero Trust | A cybersecurity strategy where all users, inside or outside the network, must be authenticated, authorized, and continuously validated before being granted or keeping access to applications and data |
| Phishing-Resistant MFA | Authentication methods that cryptographically bind authentication to the application being accessed, preventing credential forwarding or credential phishing |
| Non-Person Entity (NPE) | An automated system, service, application, or device that acts as a subject in access control decisions |
| Enterprise-Managed Identity | An identity issued and managed by the agency (or its identity provider) for official government access — not a personal or consumer identity |

---

## Key Dates and Deadlines

| Deadline | Requirement |
|---|---|
| 60 days from memo issuance (March 2022) | Submit agency Zero Trust Architecture Strategy to OMB/CISA |
| End of FY2022 (September 2022) | Initial progress report on ZT milestones |
| End of FY2024 (September 2024) | Meet all required ZT goals across five pillars |

---

## Why This Matters for RLTech

M-22-09 created an urgent, unfunded mandate for every federal civilian agency. The FY2024 deadline has passed, and many agencies did not fully achieve the required goals — particularly on phishing-resistant MFA, device compliance integration, and NPE governance. This creates significant ongoing demand for Identity pillar remediation work.

RLTech's **Zero Trust Identity Readiness Assessment** ($7,500) is specifically designed to score an agency or contractor's Identity pillar against M-22-09 requirements and produce a remediation roadmap. This is a direct product-to-mandate match.

---

## Proposal Language Anchored to M-22-09

*"This engagement addresses [Agency]'s obligations under OMB M-22-09 (Moving the U.S. Government Toward Zero Trust Cybersecurity Principles), specifically the Identity pillar requirements including phishing-resistant MFA deployment, privileged access governance, and non-person entity (NPE) lifecycle management. RLTech LLC will assess current state against the CISA Zero Trust Maturity Model Identity pillar and deliver a prioritized remediation roadmap aligned to OMB FY2024 targets."*

---

*This reference document summarizes OMB Memorandum M-22-09 (January 26, 2022) for use by RLTech LLC consultants and Dominick Skelton. Always verify against the current OMB memorandum at whitehouse.gov/omb.*
