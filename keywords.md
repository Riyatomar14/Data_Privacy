## 1. Credentials
- **Definition:** Proof that an entity (person/system) is who they claim to be.  
- **Examples:** Passwords, certificates, digital IDs.

---

## 2. Identification
- **Definition:** Process of recognizing an entity's identity.  
- **Problem:** Sending full credentials may leak sensitive info.  
- **Solution:** Minimal disclosure — share only necessary details.

---

## 3. Claims
- **Definition:** Statements about a subject that can be verified.  
- **Examples:** “Over 18”, “Has driver’s license”.

---

## 4. User Keys
- **Secret key:** Private, used for authentication/signing.  
- **Public key:** Shared, used for verification.

---

## 5. Entity Roles in DID (Decentralized Identity)
- **Issuer:** Creates & signs credentials.  
- **Holder:** Owns & presents credentials.  
- **Verifier:** Checks credentials.  
- **Storage/Verification:** Via blockchain → ensures sovereignty.

---

## 6. Identity Mixer
- Technology for **selective disclosure** of identity information.

---

## 7. Anonymous Credentials
- Hide the user’s full identity.  
- **Purpose:** Privacy protection.

---

## 8. Showing Credentials Without Losing Privacy
- Use anonymity techniques.  
- **CISO:** Chief Information Security Officer — responsible for data security.

---

## 9. Methods to Achieve Anonymity
- Group signature  
- Ring signature  
- CoinJoin  
- CoinShuffle  
- CoinSwap

---

## 10. Blind Signature
- **Definition:** Signature made without seeing the content (like signing a folded paper).  
- **Uses:** E-voting, anonymous payments.

---

## 11. Zero-Knowledge Protocols (ZKP)
### 11.1 ZKCP – Zero-Knowledge Contingent Payment
- Drawback: May require trust in intermediaries.

### 11.2 zk-SNARK
- **Example:** Zcash.  
- **Drawbacks:** Heavy computation, setup trust issues.

### 11.3 Bulletproofs
- Improves privacy but increases computation → higher energy use & latency.

---

## 12. Mixer / Tumbler
- Service that mixes cryptocurrency transactions to break traceability.

---

## 13. Monero Ring Size
- **Definition:** Number of possible senders in a transaction.  
- **Note:** Small ring size → easier de-anonymization → weakens privacy.

---

## 14. RingCT – Ring Confidential Transactions
- Hides **transaction amounts** and **sender identity**.

---

## 15. Bolt Protocol
- Protocol for **private, instant blockchain payments**.

---

## 16. Zcash
- Privacy coin using **zk-SNARKs**.

---

## 17. zk-SNARK – Four Main Ingredients
1. Encoding as a polynomial problem  
2. Succinctness via random sampling  
3. Homomorphic encryption  
4. Zero-knowledge proof  

> Popularity can influence Ethereum’s price.

---

## 18. Confidentiality
- Ensures data is only accessible to **authorized entities**.

---

## 19. Use Cases
### 19.A Anonymity
- **Examples:** Tor network, whistleblower protection platforms.  
- **Goal:** Hide **who** is involved.

### 19.B Confidentiality
- **Examples:** End-to-end encrypted messaging (Signal, WhatsApp), secure email (S/MIME, PGP), VPN, IPsec.  
- **Goal:** Protect **content** of communication.  
- **Example:** Encrypting Electronic Health Records (EHRs).

---

## 20. PRF – Pseudorandom Function
1. **Definition:** Function taking input + secret key → deterministic output that appears random.  
2. **Security:** Output indistinguishable from random without the key.  
3. **Uses:** Message Authentication Codes (MACs), Key Derivation Functions (KDFs).  
4. **Example:** HMAC (Hash-based MAC) is a PRF construction.

---

## 21. OPRF – Oblivious Pseudorandom Function
1. **Definition:** Interactive protocol — client has input, server has secret key.  
2. **Privacy Guarantee:**  
   - Client learns PRF result without seeing the key.  
   - Server learns nothing about client’s input.  
3. **Construction Methods:** Diffie-Hellman, RSA signatures, Homomorphic Encryption.  
4. **Nature:** Interactive — requires real-time collaboration.  
5. **Analogy:** Like a live interview — both sides interact to get the final result.

---

## 22. Homomorphic Encryption (HE)
1. **Definition:** Enables computation directly on encrypted data.  
2. **Types:**  
   - **PHE (Partial HE):** Supports only one operation (add/mult).  
   - **SHE (Somewhat HE):** Limited operations before noise overwhelms.  
   - **FHE (Fully HE):** Arbitrary computations possible.  
3. **Nature:** Non-interactive — encrypt once, let an untrusted party compute.  
4. **Analogy:** Like sending a sealed box with puzzle pieces — solver works without opening it.

---

## 23. Key Use Cases of PRF/OPRF/HE
1. **Private Set Intersection (PSI):** Find common data without revealing non-matching items.  
2. **Password Authenticated Key Exchange (PAKE):** Secure key exchange without revealing the password.  
3. **Token Binding / Privacy Pass:** Prove legitimacy without tracking identity.

---

## 24. Extended Applications
1. **Zero-Knowledge Proofs (ZKPs):** Prove knowledge without revealing the secret.  
2. **Authentication without password exchange:** Prevents phishing & data leaks.  
3. **Secure Multi-Party Computation (MPC):** Multiple parties jointly compute without revealing inputs.
