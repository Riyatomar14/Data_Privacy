# Key Management Lifecycle
## 1. PRE-OPERATIONAL (Plan / Generate / Register)
**Purpose:** Prepare and register keys before actual use.

### Key Generation
- Create cryptographic keys using **secure random sources**:
  - **TRNG** – True Random Number Generator  
  - **PRNG** – Pseudo-Random Number Generator  
  - **QRNG** – Quantum Random Number Generator
- **Entropy Source Validation:** Ensure entropy quality is tested (e.g., NIST SP 800-90B).  
- **Choose appropriate key size**:
  - AES: 128, 192, 256-bit  
  - RSA: 2048, 3072, 4096-bit  
  - Larger key → stronger security, slower; smaller → faster, weaker
- **Key Derivation:** Use KDFs (HKDF, PBKDF2) for session or derived keys.  
- Use strong, **compliant algorithms** (AES-256, FIPS-approved).  
- Ensure **uniqueness** of keys.  
- Use **HSMs or TPM (Trusted Platform Module)** for secure generation.  
- **Compliance Tags:** Label keys with FIPS, GDPR, PCI DSS, etc.  
- **Secure Audit Trail:** Log generation events using tamper-evident mechanisms.  
- Record **key attributes**: name, ID, creation date, cryptoperiod (validity).

### Key Registration
- Add keys to **KMS (Key Management System)** or **HSM/TPM inventory**.  
- Assign **ownership** and **access rights**.  
- **Metadata Extensions:**
  - Cryptographic algorithm & mode (AES-GCM, RSA-OAEP)  
  - Key usage flags (encrypt-only, sign-only)  
  - Lifecycle state (active, suspended, expired)  
- **Policy Binding:** Use policy engines or templates to enforce lifecycle rules.

---

## ⚙2. OPERATIONAL (Activate / Use / Maintain)
**Purpose:** Keys are active and performing cryptographic functions safely.

### Key Storage & Backup
- Store keys securely (**HSM, TPM, encrypted database**).  
- Keep **backups separate** from primary storage.  
- **Encrypted Backups:** Use KEK or envelope encryption.  
- Enable **tamper detection** on HSMs and integrity checks.  
- Consider **geo-redundant encrypted backups** for disaster recovery.  
- Conduct **regular audits** for unauthorized access or compromise.

### Key Distribution & Installation
- Manual: Use **Key Encryption Keys (KEK)** or key shares.  
- Automated: Use **asymmetric encryption / PKI**.  
- Apply **key wrapping** for safe transport.  
- **Secure Channels:** TLS 1.3 or IPsec.  
- **Certificate Pinning:** Validate public keys via pinned certificates.  
- **Zero Trust Principle:** Authenticate every access, even internal.  

### Key Use / Operation
- Perform cryptographic functions:
  - **Encrypt / Decrypt**  
  - **Sign / Verify**  
  - **MAC** (Message Authentication Code)  
- Apply **role-based & least-privilege access**.  
- **Usage Logging:** Record every operation with timestamp & actor.  
- **TPM Sealing:** Bind keys to device state using TPM sealing/unsealing.  
- **Side-Channel Protection:** Use constant-time operations to prevent timing attacks.  

### Key Rotation / Replacement
- Follow **scheduled cryptoperiod expiry**.  
- Generate **new keys**, phase out old keys.  
- Update **dependent systems and credentials**.  
- **Forward Secrecy:** Ensure new keys don’t compromise past data.  
- **Graceful Rotation:** Support dual-key operation during transition.  
- **Automated Alerts:** Notify stakeholders before cryptoperiod expiry.  
- Use **KMS automation** for rotation and revocation.

---

## 3. POST-OPERATIONAL (Deactivate / Archive)
**Purpose:** Stop key usage safely, keep records if needed.

### Key Deactivation / Expiration
- Deactivate keys when **no longer needed**.  
- **Dependency Mapping:** Identify systems, data, and users tied to the key.  
- **Soft Expiry:** Allow grace period for dependent systems to transition.  

### Key Revocation / Suspension
- Mark keys as **compromised or expired**.  
- **Revocation Lists:** Maintain/distribute CRLs or OCSP responses.  
- **Incident Response Integration:** Link revocation to security incident workflows.  

### Key Archival
- Store keys **offline, encrypted, with restricted access**.  
- Define **retention policy** based on legal and business needs.  
- **Access Controls:** Use MFA and quorum-based access for archived keys.  
- Admin can **reactivate only under strict controls**.  

---

## 4. DESTROYED (End of Life)
**Purpose:** Permanently remove key material safely.

### Key Destruction / Termination
- **Erase/overwrite** all instances of key material.  
- **Cryptographic Erasure:** Crypto-shredding for cloud-stored keys.  
- Remove **any reconstruction data** (shares, backups).  
- Require **dual-authorization** and audit confirmation.  
- **Destruction Standards:** Follow ISO/IEC 27040 and NIST SP 800-88.  
- Record **destruction details**: who, when, how.

### Regulatory Compliance
- **GDPR:** Erase keys linked to personal data on request.  
- **HIPAA:** Secure disposal of PHI encryption keys.  
- **PCI DSS:** Follow key management & destruction requirements.  
- **Audit Automation:** Use automated logging & reporting.  
- **Cross-border Considerations:** Comply with data residency laws.

  ## Abbreviations & Definitions 

| Abbreviation | Full Form | Meaning / Definition |
|--------------|-----------|----------------------|
| **KDF** | Key Derivation Function | Cryptographic function that derives one or more secret keys from a base key (e.g., HKDF, PBKDF2). |
| **HKDF** | HMAC-based Key Derivation Function |HKDF is a fast KDF for deriving multiple keys from a single high-entropy secret, such as a shared key from an Elliptic Curve Diffie-Hellman (ECDH) exchange |
| **PBKDF2** | Password-Based Key Derivation Function 2 | PBKDF2 is a slow, resource-intensive KDF designed to derive a cryptographic key from a password, making it resistant to brute-force attacks.   |
| **FIPS** | Federal Information Processing Standards | U.S. government standards for security and interoperability. |
| **GDPR** | General Data Protection Regulation | EU privacy regulation requiring secure handling and deletion of personal data. |
| **HSM** | Hardware Security Module | Dedicated secure hardware device for generating, storing, and managing cryptographic keys. |
| **TPM** | Trusted Platform Module | Security chip embedded in devices for securely storing keys and attesting platform integrity. |
| **AES-GCM** | AES Galois/Counter Mode | Authenticated encryption mode for AES providing confidentiality and integrity. |
| **RSA-OAEP** | RSA Optimal Asymmetric Encryption Padding | Padding scheme improving RSA encryption security. |
| **KEK** | Key Encryption Key | A key used to encrypt or wrap other cryptographic keys (envelope encryption). |
| **CRL** | Certificate Revocation List | List of digital certificates that have been revoked and are no longer trusted. |
| **OCSP** | Online Certificate Status Protocol | Real-time protocol to check the revocation status of a certificate. |
| **MFA** | Multi-Factor Authentication | Security method requiring more than one form of verification to access resources. |
| **Quorum Access** | — | Security approach requiring a minimum number of authorized people to approve sensitive actions. |
| **Forward Secrecy** | — | Ensures that compromise of long-term keys does not compromise past session keys. |

---
