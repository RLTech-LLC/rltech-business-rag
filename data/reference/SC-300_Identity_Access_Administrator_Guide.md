# SC-300: Microsoft Identity and Access Administrator — Study Guide
## Reference Guide for RLTech LLC

**Exam:** SC-300 — Microsoft Certified: Identity and Access Administrator Associate
**Certification:** Microsoft Certified: Identity and Access Administrator Associate
**Study guide version based on:** Microsoft exam skills outline (2024–2025)
**Exam URL:** learn.microsoft.com/en-us/credentials/certifications/identity-and-access-administrator/

---

## Why SC-300 Matters for RLTech

The SC-300 is the Microsoft certification that most directly validates RLTech's core service area. Passing SC-300 demonstrates proficiency in Microsoft Entra ID administration, Conditional Access, PIM, and Identity Governance — exactly the capabilities RLTech sells to clients. It is the single highest-ROI certification for this business.

For federal proposals and teaming agreements, having SC-300 on Dominick's capability statement strengthens technical credibility and directly supports claims about Microsoft Entra expertise.

---

## Exam Domains and Weighting

| Domain | Weight |
|---|---|
| **1. Implement and manage user identities** | 20–25% |
| **2. Implement authentication and access management** | 25–30% |
| **3. Implement access management for applications** | 15–20% |
| **4. Plan and implement identity governance** | 20–25% |

---

## Domain 1: Implement and Manage User Identities (20–25%)

### 1.1 Configure and Manage Microsoft Entra ID

- **Tenant configuration:** Default domain, tenant properties, custom domain names, tenant restrictions
- **User settings:** External collaboration settings, default user permissions, self-service settings
- **Group management:** Microsoft 365 groups, security groups, dynamic groups (attribute-based membership rules), group naming policies
- **Administrative units:** Scoped delegation of admin roles to specific subsets of users or groups
- **Roles in Entra ID:** Built-in roles (Global Admin, User Admin, Authentication Admin, etc.), custom roles, least-privilege admin design
- **Entra ID editions:** Free, P1, P2, and Governance — which features require which license

**Key skills:**
- Create and manage users (portal, PowerShell, Graph API, bulk operations via CSV)
- Create and manage groups including dynamic group rules
- Configure administrative units for scoped administration
- Manage Microsoft Entra Connect (sync configuration, filtering, attribute mapping, password hash sync, pass-through auth, seamless SSO)
- Configure Entra Cloud Sync for simpler hybrid scenarios

### 1.2 Create, Configure, and Manage Identities

- **User types:** Member users, guest users (B2B), external identities
- **B2B collaboration:** Invite guests, configure cross-tenant access settings, access packages for external users
- **Service principals:** App registrations vs. enterprise applications, client secrets, certificates, API permissions
- **Managed identities:** System-assigned vs. user-assigned; when to use managed identity vs. service principal + credential
- **Bulk operations:** Import users via CSV, bulk delete, bulk invite

**Key PowerShell cmdlets:**
```
New-MgUser, Get-MgUser, Update-MgUser, Remove-MgUser
New-MgGroup, Add-MgGroupMember
Get-MgServicePrincipal, New-MgApplication
```

### 1.3 Implement and Manage External Identities

- **B2B collaboration:** Invite external users to access internal resources; redemption flow; access package assignment
- **Cross-tenant access settings:** Inbound/outbound trust settings; MFA trust from partner tenant; device compliance trust
- **Azure AD B2C:** Customer-facing identity (different from B2B); user flows; custom policies; social identity providers
- **SAML/WS-Fed direct federation:** Federate with external organization's identity provider for guest authentication

### 1.4 Implement and Manage Hybrid Identity

- **Microsoft Entra Connect (AAD Connect):** Installation, configuration, sync rules, filtering, attribute mapping
- **Password Hash Sync (PHS):** Syncs hashed passwords to cloud; enables cloud authentication
- **Pass-Through Authentication (PTA):** Authentication forwarded to on-premises AD; no passwords in cloud
- **AD FS:** Full federation; complex; Microsoft recommends moving away from AD FS where possible
- **Seamless SSO:** Automatically signs in domain-joined Windows devices without prompting for password
- **Entra Cloud Sync:** Lighter-weight sync agent (no full AAD Connect installation); supports multi-forest; provisioning agent

---

## Domain 2: Implement Authentication and Access Management (25–30%)

### 2.1 Plan, Implement, and Manage Microsoft Entra Multi-Factor Authentication (MFA)

- **Authentication methods available:**
  - Microsoft Authenticator (push notification, number matching, passwordless phone sign-in)
  - FIDO2 security keys (phishing-resistant)
  - Windows Hello for Business (phishing-resistant, platform authenticator)
  - Certificate-based authentication (CBA) (phishing-resistant)
  - OATH hardware tokens (TOTP)
  - SMS / voice (legacy; does not meet phishing-resistant MFA requirement)
  - Temporary Access Pass (TAP) — for onboarding/recovery; time-limited
  
- **Authentication methods policy:** Configure which methods are enabled and for which users
- **MFA registration policy:** Require users to register MFA methods; combined registration experience
- **Legacy per-user MFA vs. Conditional Access MFA:** Always use Conditional Access for MFA; per-user MFA is legacy
- **MFA trusted IPs / named locations:** Define corporate network IPs; MFA may be skipped for named locations (by policy)
- **MFA in Conditional Access:** Grant control "Require multifactor authentication"

### 2.2 Plan, Implement, and Manage Passwordless Authentication

- **FIDO2 security keys:** Hardware tokens (YubiKey, etc.); most phishing-resistant; requires Entra P1+; best for shared workstations or high-privilege users
- **Windows Hello for Business (WHfB):** Platform-bound credential tied to device; uses biometric or PIN; phishing-resistant; requires P1+; best for corporate-managed Windows devices
- **Microsoft Authenticator passwordless phone sign-in:** App-based passwordless; not phishing-resistant (still vulnerable to adversary-in-the-middle); requires Authenticator app
- **Certificate-based authentication (CBA):** PIV/CAC alignment; required for full phishing-resistant MFA compliance in federal environments
- **Passkeys:** FIDO2 passkeys bound to the Authenticator app (emerging capability; phishing-resistant)

### 2.3 Plan, Implement, and Manage Self-Service Password Reset (SSPR)

- Enable SSPR for all users, selected groups, or none
- Authentication methods required for reset: mobile app code, mobile app notification, email, mobile phone, office phone, security questions
- Registration requirements: require users to register at sign-in
- SSPR writeback to on-premises AD: requires Entra Connect and appropriate license
- Disable SSPR for privileged accounts (admin accounts should not use SSPR)

### 2.4 Implement and Manage Conditional Access

**This is the highest-weight topic in Domain 2.**

- **Conditional Access policy structure:**
  - **Assignments:** Users and groups, cloud apps or actions, conditions (sign-in risk, user risk, device platforms, locations, client apps, filter for devices)
  - **Access controls:** Grant (allow with conditions: require MFA, compliant device, hybrid join, approved app, terms of use) or Block
  - **Session controls:** Sign-in frequency, persistent browser session, app enforced restrictions, Defender for Cloud Apps session controls

- **Named locations:** Define corporate IPs and compliant network locations; mark as trusted
- **Device filters:** Target specific devices by attribute (e.g., target only devices that are Entra-joined, or exclude privileged admin workstations)
- **Authentication strength:** Require specific authentication methods (e.g., phishing-resistant MFA only) rather than just "require MFA"
- **Report-only mode:** Test Conditional Access policies without enforcing them; review impact in sign-in logs
- **Break-glass (emergency access) accounts:** Exclude from all Conditional Access policies; monitor closely; rotate credentials regularly

**Common CA policy patterns:**
1. Require MFA for all users on all cloud apps
2. Require compliant or Hybrid Azure AD joined device for corporate apps
3. Block legacy authentication (Exchange ActiveSync, IMAP, POP, SMTP)
4. Require phishing-resistant MFA for privileged role activation
5. Block access from high-risk sign-in locations or sign-in risk = High
6. Require terms of use for guest users

### 2.5 Manage Microsoft Entra ID Protection

- **Risk detections:** Anonymous IP, atypical travel, malware-linked IP, unfamiliar sign-in properties, leaked credentials, password spray
- **User risk policy:** Automatically require password reset for high-risk users; configure in Conditional Access (preferred) or legacy Identity Protection policy
- **Sign-in risk policy:** Require MFA for medium/high-risk sign-ins; block high-risk sign-ins
- **MFA registration policy:** Require all users to register MFA (Identity Protection registration policy or CA)
- **Risky users report:** Review, confirm compromised, dismiss risk
- **Risky sign-ins report:** Review, confirm safe, confirm compromised

---

## Domain 3: Implement Access Management for Applications (15–20%)

### 3.1 Manage and Monitor Application Access

- **Enterprise Applications:** Pre-integrated SaaS apps from the Entra gallery; custom apps; SAML, OIDC, and legacy auth apps
- **App registration vs. Enterprise Application:** App registration = developer registration; Enterprise Application = service principal (the instance of the app in the tenant)
- **User assignment:** Require user assignment for apps; assign users/groups to apps
- **App roles:** Define custom roles within an application; assign users to roles
- **Microsoft Defender for Cloud Apps (MDCA/CASB):** Discover shadow IT; enforce session controls on SaaS apps; monitor file access
- **Conditional Access app control (session proxy):** Route app traffic through MDCA for real-time session monitoring and control

### 3.2 Plan, Implement, and Monitor the Integration of Enterprise Apps for SSO

- **SAML SSO:** Configure SAML-based SSO for non-gallery and gallery apps; claims transformation; signing certificates
- **OIDC/OAuth SSO:** Modern apps using OpenID Connect; client credentials flow, authorization code flow, on-behalf-of flow
- **Password-based SSO:** For legacy apps that cannot support modern protocols; credentials vaulted in Entra
- **Linked SSO:** Point to an existing SSO provider; no authentication handled by Entra
- **Application Proxy:** Publish on-premises web apps through Entra Application Proxy for remote access without VPN; supports Kerberos constrained delegation (KCD) for SSO to on-premises apps

### 3.3 Implement and Manage App Registrations

- **App registration components:** Application ID, client secrets, certificates, redirect URIs, API permissions
- **API permissions:** Delegated (user context) vs. Application (daemon/service context); admin consent required for application permissions
- **Expose an API:** Define scopes for your app that other apps can request
- **Certificates vs. client secrets:** Always prefer certificates over client secrets for production apps; use Managed Identity where possible

---

## Domain 4: Plan and Implement Identity Governance (20–25%)

### 4.1 Plan and Implement Entitlement Management

- **Access packages:** Bundle of resources (groups, apps, SharePoint sites, roles) that can be requested by users; includes assignment policies, approval workflows, and expiration
- **Catalogs:** Containers for access packages; scope which resources and which requestors
- **Assignment policies:** Who can request (specific users, all members, guests); approval stages (manager, sponsor, auto-approve); expiration and renewal
- **Connected organizations:** Allow users from partner organizations to request access packages (B2B governance)
- **Use case:** Onboard contractors with time-limited access to specific applications via access package request

### 4.2 Plan, Implement, and Manage Access Reviews

- **Access reviews:** Periodic review of group memberships, app assignments, role assignments, or access package assignments
- **Reviewers:** Self-review, manager review, designated reviewer(s), group owners
- **Auto-apply results:** Automatically remove access if reviewer says "Deny" or doesn't respond
- **Insights and recommendations:** AI-driven recommendations for reviewers (e.g., "Last signed in 90 days ago — recommend deny")
- **Use case:** Quarterly review of users assigned to privileged roles; annual review of all guest user access

### 4.3 Plan and Implement Privileged Identity Management (PIM)

**This is one of the highest-priority topics for RLTech's service offerings.**

- **PIM-eligible vs. active assignments:**
  - **Eligible:** User has the right to activate the role on-demand; not persistently active
  - **Active:** Role is always active; avoid for privileged roles
  - **Time-bound:** Both eligible and active assignments can have expiration dates

- **Role activation:**
  - User requests activation in the Entra portal or via Authenticator app
  - Justification required (configurable)
  - MFA or authentication strength required at activation (configurable)
  - Maximum activation duration (configurable; e.g., 8 hours for Global Admin)
  - Approval required (configurable; specify approver)
  - After activation, role is active for the configured duration

- **PIM policies (role settings):**
  - Maximum activation duration
  - Require MFA on activation
  - Require justification on activation
  - Require approval (and specify approvers)
  - Notification on activation (to role owner, admin)
  - Require access review for eligible assignments

- **PIM for Azure resources:** Same JIT model applied to Azure RBAC roles (Owner, Contributor, etc.)
- **PIM for Groups:** Activate group membership on a JIT basis; useful for groups that grant access to apps or resources
- **Access reviews in PIM:** Periodic review of eligible and active role assignments; auto-remove if not confirmed

- **Break-glass accounts:**
  - 2 cloud-only Global Administrator accounts
  - Excluded from all Conditional Access policies (including MFA requirements)
  - Credentials stored offline (password written on paper in a safe)
  - Hardware FIDO2 key as authentication method (not phone-based)
  - Sign-in monitored with high-severity alert
  - NOT enrolled in PIM (must be always-active Global Admin)

### 4.4 Monitor and Maintain Microsoft Entra ID

- **Audit logs:** All changes to the directory (user creation, role assignment, policy changes); retain 30 days free (Entra P1/P2)
- **Sign-in logs:** All sign-in events including interactive, non-interactive, and service principal sign-ins; 30-day retention
- **Provisioning logs:** Activity from automated provisioning (SCIM, Entra provisioning)
- **Identity Secure Score:** Percentage score of implemented security recommendations; actionable improvement items
- **Diagnostic settings:** Export logs to Log Analytics workspace, Storage Account, or Event Hub for long-term retention and SIEM integration
- **Microsoft Sentinel:** Connect Entra ID via data connector; use built-in analytics rules for identity threats; KQL for custom detection
- **Workbooks:** Pre-built monitoring dashboards for Entra (risky users, CA coverage, sign-in analysis)

---

## Key Licensing Requirements

| Feature | License Required |
|---|---|
| Basic MFA (Security Defaults) | Free |
| Conditional Access | Entra P1 |
| Entra ID Protection | Entra P2 |
| PIM | Entra P2 |
| Access Reviews | Entra P2 (or Entra ID Governance) |
| Entitlement Management | Entra ID Governance |
| Lifecycle Workflows | Entra ID Governance |
| Entra Workload Identities | Entra Workload Identities license |
| FIDO2 / Passwordless | Entra P1 |
| Certificate-Based Authentication (CBA) | Free (for federated) / P1 for cloud |
| Cross-Tenant Access Settings | P1 |

---

## Common Exam Gotchas

1. **Legacy per-user MFA vs. Conditional Access MFA** — Microsoft recommends Conditional Access for MFA enforcement. Per-user MFA is a legacy approach and is being phased out. CA MFA does NOT combine well with per-user MFA.

2. **Break-glass accounts** — Must be cloud-only (not synced from on-premises AD), must be excluded from Conditional Access (especially MFA), and must be monitored. These are different from emergency access PIM activation.

3. **Managed Identity vs. Service Principal + Secret** — Always recommend Managed Identity (no credential to manage or leak). Service principal + client secret is the less secure option.

4. **PIM eligible vs. PIM active** — Eligible means the user CAN activate the role; active means they currently have the role. Persistent active assignment is the anti-pattern for privileged roles.

5. **Authentication strength vs. Require MFA** — Authentication strength is the more granular control; it lets you require phishing-resistant MFA (not just any MFA method). Use authentication strength for privileged role activation.

6. **SSPR writeback** — Requires Entra Connect (or Cloud Sync) AND Entra P1 license. If writeback is not configured, users can reset cloud passwords but it does not change the on-premises AD password.

7. **Report-only mode** — Use this to test Conditional Access policies before enabling them. Policies in report-only mode are evaluated but not enforced; results appear in sign-in logs.

---

## Study Resources

- **Microsoft Learn:** learn.microsoft.com → Certifications → SC-300 — free, comprehensive, hands-on labs
- **Practice assessments:** Free practice assessment linked from the SC-300 certification page
- **Entra admin center:** entra.microsoft.com — hands-on practice in a dev/test tenant (free M365 Developer Program tenant)
- **Microsoft 365 Developer Program:** developer.microsoft.com/microsoft-365/dev-program — free E5 tenant for 90 days (renewable) with all Entra P2 features

---

*This reference document is a study guide for the SC-300 Microsoft Identity and Access Administrator certification for use by Dominick Skelton / RLTech LLC. Always verify current exam skills outline at learn.microsoft.com as Microsoft updates exam content periodically.*
