# 1. Key Management Lifecycle
##  The Seed — Where It All Begins
Every secure cryptographic system starts with **randomness** — and at the heart of that is the **seed**.  
A **seed** is the first unpredictable value that drives a **Pseudo-Random Number Generator (PRNG)** or feeds into a **Deterministic Random Bit Generator (DRBG)**.  

Key characteristics of a good seed:
- **High entropy:** unpredictable, ideally from TRNG/QRNG or TPM.
- **Unique:** never reuse seeds between systems.
- **Protected:** store and handle like a cryptographic key.
- **Refreshed:** reseed periodically to maintain unpredictability.
  
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

## 2. OPERATIONAL (Activate / Use / Maintain)
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

## FLOW-CHART

![WhatsApp Image 2025-09-13 at 20 40 01_cb292bf8](https://github.com/user-attachments/assets/b8777ba2-9a3d-48be-b383-a1707236e69d)

# 2. Key Exchange (KEX)

Key Exchange (or **Key Establishment**) = the process of securely creating a **shared secret key** between two parties over an insecure channel.

---

## 1️⃣ Background

- Before public-key cryptography, only **symmetric keys** existed.
- **Problem:** Both parties needed the **same secret key** but had no secure way to exchange it over the internet.
- Early systems used trusted couriers or diplomatic channels, which were risky.

---

## 2️⃣ From Symmetric to Asymmetric

| Feature | Symmetric | Asymmetric |
|----------|-----------|------------|
| Key Ownership | One secret key shared by both parties | Each party has its own public/private key pair |
| Key Distribution | Must be pre-shared securely | Public key can be shared openly; private key stays secret |
| Speed | Faster once key known | Solves the key distribution problem |

---

## 3️⃣ Why KEX Matters

- Builds secure channels over insecure networks.
- Enables **session keys** for confidentiality, integrity, and forward secrecy.
- Underpins protocols like **TLS, SSH, IPsec, Signal**.

---

## 4️⃣ Types of Key Exchange

### (A) Classical KEX

- **Diffie–Hellman (DH):**
  - Classic large-prime exchange.
  - Vulnerable to MITM if unauthenticated.
  - Legacy TLS / VPNs.
- **Ephemeral DH (DHE):**
  - New key per session → forward secrecy.
- **Elliptic Curve DH (ECDH):**
  - Same concept on elliptic curves → smaller keys, faster.
  - TLS 1.3, SSH, Signal.
- **Ephemeral ECDH (ECDHE):**
  - Adds forward secrecy to modern secure protocols.

---

### (B) Public-Key Based KEX

- **RSA Key Exchange:** Encrypts a random session key with receiver’s public key (older TLS).
- **RSA-KEM:** Key Encapsulation Mechanism using RSA to wrap a session key.

---

### (C) Post-Quantum KEX

- **Kyber:** Lattice-based, NIST finalist, quantum-resistant.
- **NewHope:** Ring-LWE, experimental TLS research.
- **FrodoKEM:** Conservative LWE, larger but robust.

---

### (D) Hybrid KEX

- Combines classical + post-quantum.
- Example: **ECDHE + Kyber** ensures security even if one fails.
- Already used in post-quantum TLS handshakes.

---

## 5️⃣ How Diffie–Hellman Works (Classic Example)

1. Agree on **p** (prime modulus) and **g** (generator).
2. Each party picks a **private exponent**.
3. Compute public value `A = g^a mod p` and `B = g^b mod p`.
4. Exchange A and B over the network.
5. Compute shared secret:
   - Alice: `S = B^a mod p`
   - Bob: `S = A^b mod p`
6. Both derive same `S`; optionally run through a **KDF** for a session key.

**Benefits:**  
- No secret key transmitted directly.  
- Forward secrecy with ephemeral keys.  

---
---
## FLOW-CHART
![WhatsApp Image 2025-09-13 at 21 53 12_71e37ebc](https://github.com/user-attachments/assets/48691013-74e4-42f1-b00c-317de9fcba75)

# 3. Key Encapsulation Mechanism (KEM)

A **KEM** is a cryptographic primitive to securely deliver a **session key** to a receiver using **public-key cryptography**.

---

## 1️⃣ Why KEM Exists

- Public-key encryption of large data is inefficient.
- KEM exchanges only a small **session key** securely.
- Once shared, that session key is used with **fast symmetric encryption**.

---

## 2️⃣ Three Core Algorithms in KEM

### (A) Key Generation — `KeyGen()`
- Run by **Receiver**.
- Output: `(pk, sk)` public and private key pair.

### (B) Encapsulation — `Encapsulate(pk)`
- Run by **Sender** using Receiver’s `pk`.
- Output: `(c, K)`:
  - `c` = ciphertext encapsulation of key.
  - `K` = session key.

### (C) Decapsulation — `Decapsulate(c, sk)`
- Run by **Receiver**.
- Input: `c` and `sk`.
- Output: session key `K`.

---

## 3️⃣ Protocol Flow of KEM

1. **Receiver → KeyGen()** → `(pk, sk)`.
2. **Receiver → publishes pk**.
3. **Sender → Encapsulate(pk)** → `(c, K)`.
4. **Sender → sends c**.
5. **Receiver → Decapsulate(c, sk)** → `K`.
6. **Both now share K** (used for symmetric encryption).

---

## 4️⃣ Security Properties of KEM

- **Confidentiality:** Only Receiver can recover `K`.
- **Indistinguishability:** `K` appears random to outsiders.
- **Robustness:** Even if some values leak, `sk` stays secure.
- **Efficiency:** Symmetric encryption with `K` is much faster than encrypting full data with public-key cryptography.

---

## 5️⃣ Applications of KEM

- **TLS 1.3 / HTTPS** (post-quantum handshakes).
- **VPNs / SSH** secure channel key establishment.
- **Hybrid encryption schemes** (Public Key = KEM, Symmetric Key = DEM).

---

## 6️⃣  Text Tree of KEM

<img width="397" height="481" alt="image" src="https://github.com/user-attachments/assets/30b74e6b-88d9-4464-a5a2-e0c126b46681" />


## 7️⃣ Visual Diagram
![WhatsApp Image 2025-09-13 at 21 59 53_4f6f0c70](https://github.com/user-attachments/assets/d61278c1-a5ea-4434-81ef-7f20922d2391)

---
## KEX VS KEM

| Feature                      | **KEX (Key Exchange)**                                                                                      | **KEM (Key Encapsulation Mechanism)**                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Goal**                     | Two parties *jointly derive* a shared secret (session key) without transmitting it directly.                | Sender *creates or encrypts* a random session key and securely delivers it to Receiver.                                   |
| **Main Idea**                | Each party contributes secret material → both compute same key locally.                                     | Receiver generates public/private key pair → Sender uses public key to encapsulate a session key → Receiver decapsulates. |
| **Key Creation**             | Key is **computed** by both sides from their private key + other party’s public key. (e.g., Diffie–Hellman) | Key is **generated by Sender** and then **encapsulated** to Receiver using Receiver’s public key.                         |
| **Algorithms Used**          | Diffie–Hellman (DH/DHE), Elliptic Curve DH (ECDH/ECDHE), Hybrid (ECDHE + Kyber).                            | RSA-KEM, Kyber, NewHope, FrodoKEM, Hybrid KEM.                                                                            |
| **Public/Private Keys**      | Both sides generate public/private keys for exchange.                                                       | Only the Receiver generates a public/private key pair; Sender just uses public key to encapsulate.                        |
| **Session Key Transmission** | No key is sent directly — only public parameters exchanged.                                                 | A ciphertext (encapsulation) is sent containing the session key.                                                          |
| **Security Basis**           | Hardness of **Discrete Logarithm** (or Elliptic Curve DL) or PQ equivalents.                                | Hardness of **lattice/RSA** or other PQ assumptions depending on KEM.                                                     |
| **Speed**                    | Usually faster in classic settings; simple math but needs both sides to compute.                            | Encapsulation/decapsulation is one-shot; can be more efficient for bulk data after key exchange.                          |
| **Use in Protocols**         | TLS 1.2/1.3 (ECDHE), SSH, IPsec.                                                                            | Post-quantum TLS (Kyber), RSA-KEM in hybrid systems.                                                                      |
| **When Preferred**           | When you want **mutual contribution** and **forward secrecy**.                                              | When you want **one-way key delivery** and **simple session key establishment**.                                          |

---

# 4.Hashing  

## 1️⃣ Introduction  
A **hash function** is a mathematical function that takes an input (any size) and produces a fixed-size output called a **hash**, **digest**, or **fingerprint**.  
Hashing is a **one-way** process — it’s easy to compute a hash from data but infeasible to reconstruct the original data from the hash.

---

## 2️⃣ Why Hashing Matters  
- **Data integrity:** Detects changes in files or messages.  
- **Password security:** Stores password hashes instead of plaintext.  
- **Digital signatures:** Hash data before signing.  
- **Efficient comparison:** Hash values make data lookup faster.  
- **Blockchain:** Links blocks using cryptographic hashes.  

---

## 3️⃣ Hash Function Working  

### Flow  

<img width="704" height="53" alt="image" src="https://github.com/user-attachments/assets/f1aadc8f-1d82-465f-9a49-7e4b6977f79c" />


---

## 4️⃣ Core Properties of Cryptographic Hash Functions  

| Property | Description |
|-----------|-------------|
| **Deterministic** | Same input → always same hash. |
| **Preimage Resistance** | Given `h = H(x)`, infeasible to find `x`. (One-way property). |
| **Second Preimage Resistance** | Given `x1`, infeasible to find `x2 ≠ x1` such that `H(x1) = H(x2)`. |
| **Collision Resistance** | Infeasible to find *any* two distinct inputs producing same hash. |
| **Avalanche Effect** | Small input change → drastically different hash. |
| **Efficiency** | Fast to compute for large data. |
| **Fixed Output Size** | Output always a fixed length regardless of input size. |

---

## 5️⃣ Types of Hash Functions  

### 🔹 Non-Cryptographic Hashes  
Used for data structures (hash tables), not security:  
- MurmurHash  
- FNV  
- CityHash  

### 🔹 Cryptographic Hashes (Security Focused)  
- **MD5** (128-bit, broken — use only for non-security purposes)  
- **SHA-1** (160-bit, broken for collisions)  
- **SHA-2 Family:** SHA-224, SHA-256, SHA-384, SHA-512 (widely used)  
- **SHA-3 (Keccak):** New standard, sponge construction  
- **BLAKE2 / BLAKE3:** Fast, secure modern hashes  

---

## 6️⃣ Hashing Algorithms: Construction Styles  

| Construction | Example | How it Works |
|--------------|---------|--------------|
| **Merkle–Damgård** | MD5, SHA-1, SHA-2 | Processes input in fixed-size blocks using a compression function. |
| **Sponge Construction** | SHA-3 / Keccak | Absorbs input then squeezes out fixed-size output. |
| **Tree Hashes** | BLAKE3, parallelized SHA | Splits data into chunks, hashes in parallel, combines in a tree. |

---

## 7️⃣ Hash-Based Cryptographic Primitives  

| Primitive | Explanation |
|-----------|-------------|
| **HMAC (Hash-based Message Authentication Code)** | Combines a secret key + hash to authenticate messages. |
| **HKDF (Hash-based Key Derivation Function)** | Derives cryptographic keys from a shared secret. |
| **Digital Signatures** | Data is hashed first, then signature generated on hash. |
| **Commitment Schemes** | Commit to a value while keeping it hidden using a hash. |

---

## 8️⃣ Password Hashing (Important Distinction)  
Plain hash functions alone are **not enough** for passwords.  
Use **specialized password hashing algorithms** designed to be slow & memory-hard:  
- **bcrypt**  
- **scrypt**  
- **Argon2** (modern, NIST-recommended)  

---

## 9️⃣ Real-World Applications of Hashing  

| Area | Use Case |
|-------|----------|
| **Data Integrity** | File verification (SHA-256 checksums). |
| **Digital Signatures** | Hash before signing. |
| **Blockchain / Cryptocurrency** | Linking blocks (Bitcoin uses SHA-256). |
| **Certificates / PKI** | Hashing public keys in X.509 certs. |
| **Message Authentication** | HMAC in TLS, SSH. |

---

## 🔟 Security Considerations  

- **MD5 & SHA-1 are deprecated** — vulnerable to collision attacks.  
- Always use **salt** with password hashing to prevent rainbow table attacks.  
- Use **keyed hashing (HMAC)** for authentication.  
- Pick algorithms with strong **cryptanalysis history** (SHA-2, SHA-3, BLAKE2).
  
### Salt in Hashing   
A **salt** is a random value added to an input **before hashing**.  
It ensures that even if two users have the same password, their hashes are different.  
Salts defend against **rainbow table** and **precomputation attacks**.

##### Salted Hashing Flow  
Password + Random Salt ──► Hash Function ──► Salted Hash
Store: (Salt, Hash)

##### Why Salt is Important  
- Without a salt: Same password → same hash.  
- With a salt: Same password → different hashes per user.  
---

## Visual Overview  

### Hash Function Flow Diagram  
<img width="385" height="331" alt="image" src="https://github.com/user-attachments/assets/2922f0e4-62a4-4073-ac1d-4dc2c48e9d09" />

## Avalanche-Effect
-Input1: "Hello"
-SHA-256: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969

-Input2: "hello"  (changed only 'H'→'h')
-SHA-256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

## Message Digest, Integrity & Confidentiality

### Message Digest
A **Message Digest** is the fixed-length output of a cryptographic hash function (like **SHA-256**).  
It represents the **fingerprint** of the original message.

- Input: Any length message.
- Output: Fixed-length hash (e.g., 256 bits for SHA-256).
- Purpose: Verify data **integrity** and support **authenticity**.

---

## 2. Integrity vs. Confidentiality

| Property        | What It Means                                                                 |
|-----------------|-------------------------------------------------------------------------------|
| **Integrity**   | -The **hash verifies** the message hasn’t changed (integrity).          |
| **Confidentiality** | The **encryption hides** the message (confidentiality).                 |

- **Hash/Message Digest alone → Integrity.**
- **Encryption (symmetric/asymmetric) → Confidentiality.**
- Combine them (encrypt + hash) to get **both**--> HASH.

---

## 3. Sender → Receiver Flow with Message Digest (Integrity)
<img width="567" height="637" alt="image" src="https://github.com/user-attachments/assets/d8a65b72-5152-4a62-8127-cf04b4eaaabf" />

## Receiver Side (Confidentiality)
<img width="543" height="716" alt="image" src="https://github.com/user-attachments/assets/aa06719c-2bf7-422d-b596-8d02cd378566" />

-Compare H and H' at Receiver:
  - If equal → Integrity OK.
  - If different → Message tampered.













