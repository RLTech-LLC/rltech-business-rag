# NIST SP 800-207 — Zero Trust Architecture
## Reference Guide for RLTech LLC

**Source:** National Institute of Standards and Technology (NIST) Special Publication 800-207
**Title:** Zero Trust Architecture
**Published:** August 2020
**Authors:** Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly

---

## What Is Zero Trust?

Zero Trust (ZT) is a cybersecurity paradigm focused on resource protection with the premise that trust is never implicitly granted based solely on network location or asset ownership. Zero Trust requires that all access requests be continuously verified regardless of whether they originate from inside or outside the traditional network perimeter.

**Core premise:** "Never trust, always verify."

Zero Trust Architecture (ZTA) is an enterprise cybersecurity architecture based on Zero Trust principles. It is designed to prevent unauthorized access to data and services by making access control decisions as granular as possible.

---

## The Seven Tenets of Zero Trust (NIST SP 800-207, Section 2)

1. **All data sources and computing services are considered resources.**
   Every device, user, application, and service is a potential resource — including BYOD devices, IoT, cloud services, and remote workers. There is no implicit difference between "on-network" and "off-network" resources.

2. **All communication is secured regardless of network location.**
   Network location alone does not imply trust. All communication must be secured (authenticated, authorized, encrypted) regardless of whether the traffic is inside or outside the enterprise network perimeter.

3. **Access to individual enterprise resources is granted on a per-session basis.**
   Trust granted to a subject during one session is not automatically extended to subsequent sessions or to other resources. Access must be re-evaluated for each session.

4. **Access to resources is determined by dynamic policy.**
   Policy is defined by the organization and uses attributes of the requesting subject (user identity, device state, behavioral patterns), the requested resource, and the environment (time, location, threat intelligence). Policy is applied dynamically at the moment of access.

5. **The enterprise monitors and measures the integrity and security posture of all owned and associated assets.**
   No device is assumed to be fully trusted. Asset posture is continuously monitored and factored into access decisions.

6. **All resource authentication and authorization are dynamic and strictly enforced before access is allowed.**
   Continuous authentication and re-authorization cycle is the norm. Subjects must re-authenticate or re-authorize as risk signals change.

7. **The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications and uses it to improve its security posture.**
   Data collection, analytics, and feedback loops are essential to a functioning ZTA.

---

## Logical Components of a ZTA (Section 3)

Zero Trust Architecture has three primary logical components:

### Policy Engine (PE)
The ultimate decision point for granting or denying access to a resource. The PE uses enterprise policy, threat intelligence feeds, CDM data, and identity data to grant, deny, or revoke access. The PE records its decisions for audit purposes.

### Policy Administrator (PA)
Executes the Policy Engine's access decisions. The PA establishes or shuts down the communication path between a subject and a resource. It generates session-specific credentials or tokens needed for access. Communicates with the Policy Enforcement Point.

### Policy Enforcement Point (PEP)
The component that enables, monitors, and terminates connections between subjects and enterprise resources. Receives instructions from the Policy Administrator to allow or deny communications.

**Data flows:**
- Subject → PEP → PA → PE → (policy stores, CDM, threat intelligence, identity governance)
- PE makes decision → PA → PEP enforces decision → Subject accesses or is denied resource

---

## Trust Algorithm (Section 3.1)

The Trust Algorithm is the process the Policy Engine uses to make access decisions. Inputs include:

- **Subject database (IAM system)** — User identity, role, assigned attributes, privileges
- **Asset database (CDM/CMDB)** — Device status, patch level, software, security posture
- **Resource requirements** — Sensitivity classification of the requested resource
- **Environmental conditions** — Time of day, geolocation, network (on-prem, cellular, hotel WiFi)
- **Behavioral/threat intelligence** — Anomaly detection, UEBA, threat feeds, past access patterns
- **Activity logs** — Historical access patterns for this subject

The Trust Algorithm compares the input against policy to produce a score or decision: allow, deny, or allow with conditions (e.g., step-up authentication required).

---

## ZTA Deployment Scenarios (Section 4)

### 4.1 Device Agent / Gateway-Based Deployment
An agent installed on enterprise devices communicates with a gateway that enforces access decisions. Most applicable to managed device fleets. The agent reports device state to the PA.

### 4.2 Enclave-Based Deployment
Resources are organized into micro-perimeters (enclaves). PEPs control access to each enclave. Useful when device agent deployment is impractical (legacy systems, IoT, or partner access).

### 4.3 Resource Portal-Based Deployment
A portal acts as the PEP for a set of resources. Users authenticate to the portal, which grants or denies access to specific resources behind it. Most applicable for remote access and externally-facing resources.

### 4.4 Device Application Sandbox / Service Mesh
Applications running in a cloud or container environment enforce ZT through service-to-service policies. Relevant for microservices architectures and DevSecOps environments.

---

## ZTA and Identity (IAM Implications)

IAM is the foundation of Zero Trust. NIST 800-207 explicitly identifies the identity plane as the core control surface. Key IAM requirements for ZTA:

- **Strong, verifiable identity for all subjects** — User accounts must use phishing-resistant MFA. Machine identities (service accounts, managed identities) must be governed and inventoried.
- **Just-in-time (JIT) and just-enough-access (JEA)** — Persistent privileged access is a ZT antipattern. PIM / JIT access is the ZT-aligned model.
- **Continuous authorization** — Token lifetimes should be short. Continuous Access Evaluation (CAE) in Microsoft Entra implements this.
- **Identity as the new perimeter** — In a ZTA, the identity of the subject and the posture of their device are the primary inputs to access decisions, not network location.
- **Non-human identities** — Service principals, managed identities, and automated pipelines are subjects in a ZTA and must be governed under the same principles. This is frequently overlooked.

---

## Microsoft Implementation Alignment

| ZTA Concept | Microsoft Entra / M365 Implementation |
|---|---|
| Policy Engine | Conditional Access policies + Entra ID Protection |
| Policy Enforcement Point | Entra ID sign-in process; App Proxy; PIM activation gate |
| Strong identity for users | Phishing-resistant MFA (FIDO2 / Windows Hello) |
| Device posture | Intune device compliance + Conditional Access device filter |
| JIT privileged access | Entra PIM (eligible roles, time-limited activation) |
| Continuous authorization | Continuous Access Evaluation (CAE) + sign-in frequency policies |
| Non-human identity governance | Entra Workload Identities; Managed Identity for Azure resources |
| Behavioral analytics | Microsoft Entra ID Protection (risk signals) + Microsoft Sentinel |

---

## ZTA Migration Approaches (Section 7)

NIST identifies three migration strategies:

1. **Identity-based ZTA (Plant the flag)** — Start with identity as the control plane. Implement strong MFA, PIM, Conditional Access first. This is the most common and recommended starting point for federal agencies.

2. **Micro-segmentation** — Divide the network into micro-perimeters and enforce access controls at each boundary. More applicable to network/infrastructure teams.

3. **Network Infrastructure and Software Defined Perimeters (SDP)** — Full software-defined networking implementation. Higher maturity, more complex.

For most federal agencies at Initial or Traditional ZTMM maturity: **start with Identity**.

---

## Federal Application

NIST SP 800-207 is the foundational document for federal Zero Trust initiatives. It is referenced directly in:
- **OMB M-22-09** (Moving the U.S. Government Toward Zero Trust Cybersecurity Principles) — agencies required to meet ZT goals aligned to NIST 800-207 architecture
- **CISA Zero Trust Maturity Model** — explicitly uses NIST 800-207 pillars as the foundation
- **DoD Zero Trust Strategy** — references NIST 800-207 principles
- **EO 14028** (Executive Order on Improving the Nation's Cybersecurity) — directed agencies to adopt ZT architecture per NIST guidance

---

## Key Quotes for Use in Proposals / Client Engagements

> "Zero trust is a response to enterprise network trends that include remote users, bring your own device (BYOD), and cloud-based assets that are not located within an enterprise-owned network boundary." — NIST SP 800-207, p.1

> "No implicit trust is granted to assets or user accounts based solely on their physical or network location (i.e., local area networks versus the internet) or based on asset ownership (enterprise or personally owned)." — NIST SP 800-207, p.4

> "All communication must be done in the most secure manner available, including using the latest version of Transport Layer Security (TLS) where applicable." — NIST SP 800-207, Tenet 2

---

*This reference document summarizes NIST SP 800-207 (August 2020) for use by RLTech LLC consultants and Dominick Skelton in client engagements, proposal writing, and professional development. Always verify against the current published version at csrc.nist.gov.*
