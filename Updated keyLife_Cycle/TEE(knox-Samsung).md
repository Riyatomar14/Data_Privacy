# Samsung-Knox

<img width="1536" height="1024" alt="ChatGPT Image Sep 27, 2025, 01_01_08 PM" src="https://github.com/user-attachments/assets/dc330891-529b-4c69-a47f-8135fe0bd4ec" />


## What is Samsung Knox?
Samsung Knox is a **mobile security platform** built into Samsung Galaxy devices. It provides a **secure environment** for corporate data, apps, and personal information **without third-party IT security solutions**. Knox ensures that your device is **protected from the moment it powers on**, using multi-layered security measures.

---

## Why is Samsung Knox Required?
1. **Mobile devices are prime targets:** Smartphones and tablets contain sensitive personal and corporate data, making them attractive to cybercriminals.  
2. **Growing mobile usage:** The increase in mobile device use has made security more critical.  
3. **Factory-level security:** Samsung creates a **device root key** and a **device-unique hardware key** at manufacture. These are **public/private key pairs stored in the Trusted Execution Environment (TEE)**. Access is tightly regulated.  
4. **Foundation for Knox features:** These keys are the basis for the platform’s advanced security features, protecting both **personal and corporate data**.

---

## Samsung Knox vs Other Device Security

| Feature / Security Layer       | Other Devices               | Samsung Knox                     |
|--------------------------------|----------------------------|----------------------------------|
| Device Root / Hardware Key      | Limited or none            | Device-unique keys in TEE        |
| Kernel Protection               | Not always protected       | Runtime Kernel Protection (RKP)  |
| Boot Integrity                  | Basic Secure Boot          | Secure Boot & Trusted Boot       |
| Data Protection                 | Standard encryption        | Hardware-backed encryption & Knox Vault |
| Corporate App Security          | Limited                    | Secure Workspace / Containerization |

**Why Kernel Protection Matters:**  
- The kernel is the **core of the operating system**.  
- A compromised kernel can leak sensitive data, allow remote monitoring, and compromise enterprise data integrity.  
- Knox Runtime Kernel Protection (RKP) actively **monitors and prevents kernel-level attacks**.

---

## Full Security Coverage
Samsung continuously updates Knox with the **latest runtime protections** and new security capabilities, including:
- **Device integrity** (Secure Boot, Trusted Boot)  
- **Data protection** (encryption, key management)  
- **App and container security** (secure workspace for corporate apps)  
- **Real-time kernel protection** (RKP)

---

## Key Features of Samsung Knox
1. **Hardware Root of Trust** – Device-unique keys stored in TEE.  
2. **Secure Boot & Trusted Boot** – Ensures device boots only trusted software.  
3. **Knox Vault** – Isolated, tamper-proof storage for sensitive data.  
4. **Runtime Kernel Protection (RKP)** – Detects and prevents kernel-level attacks.  
5. **Containerization** – Keeps corporate and personal data separate.  
6. **Remote Management & Enterprise Support** – IT admins can enforce policies securely.





## How Knox Encrpt data 
<img width="1343" height="977" alt="Screenshot 2025-09-28 221716" src="https://github.com/user-attachments/assets/328a051a-9e99-4bf9-9d20-cf822523d7ca" />

# 🔒 Encryption Flow 

This document explains how **Samsung Knox** encrypts data inside its secure environment, step by step.  
It uses **simple language** but follows the **real flow of Android + Knox hardware**.

---

## 1. App (Normal World)

Your app (banking app, gallery, etc.) runs in the **normal Android environment**.  
It wants to store or send some sensitive data securely (like a password or token).  
It does **not** encrypt the data itself; it asks **Knox/KeyStore** to do it.

---

## 2. Calls Android KeyStore / Knox Keystore HAL API

The app calls special system APIs provided by Android/Knox (**KeyStore** or **Knox HAL**).  
These APIs are like a **security service counter** — the app hands over data and a **key handle**.  
The app never touches the **real cryptographic key**; it only passes a **reference**.

---

## 3. Packages Data + Key Handle into Secure Request

The KeyStore HAL takes the app’s **plaintext data** and the **key handle** (not the key itself).  
It wraps them in a **secure message**.  
This message is prepared to be sent into the secure part of the device.

---

## 4. Kernel Trusted Driver (/dev/qseecom or /dev/tzdev)

This is a **special kernel driver** that connects Android to the **secure processor (TEE)**.  
It acts like a **tunnel** — only trusted system services can use it.  
No normal app can talk directly to the TEE.

---

## 5. Allocates Shared Memory Buffer

Before sending data to the TEE, the driver sets up a **shared memory region**.  
This is a protected area both Android and the TEE can read/write.  
Data is copied here temporarily, but keys still stay in the TEE.

---

## 6. Secure Monitor Call (SMC) → Switch CPU to TEE (Secure World)

The driver sends an **SMC instruction** to the CPU.  
This tells the processor: “Switch from **Normal World** to **Secure World**.”  
Now the CPU runs in **secure mode** and executes code from the TEE instead of Android.

---

## 7. TEE Trusted App (Keymaster / Knox)

Inside the **TEE (Trusted Execution Environment)** lives a small **trusted app** — in Android this is called **Keymaster**, in Samsung Knox it’s part of **Knox Vault**.  
This trusted app is **isolated, signed, and cannot be modified by hackers**.

---

## 8. Policy & Integrity Check

Before doing any cryptographic operation, the TEE checks device integrity:

- **Secure Boot verified?** – Ensures firmware hasn’t been modified.  
- **Tamper sensors OK?** – Checks voltage, glitch, laser, and temperature sensors.  

If any check fails, the TEE can **refuse to process** or **wipe keys**.  
This is why Knox can detect tampering and **trip e-fuse flags**.

---

## 9. Key Retrieval from Knox Vault (Secure Storage)

If the integrity checks pass, the TEE fetches the cryptographic key from **Knox Vault**.  
The key lives only in **secure hardware storage** (separate chip/region).  
The **real key never leaves** the secure world — only a **handle/reference** is known outside.

---

## 10. Encryption Operation (AES / RSA / ECC inside TEE Memory)

Inside TEE memory, the plaintext from the app is combined with the key to do **encryption**.  
This could be **symmetric (AES)** or **asymmetric (RSA/ECC)**.  
Because it’s all inside the TEE, the plaintext and the key are **never exposed** to Android.  

The **plaintext → ciphertext** transformation happens entirely **inside secure memory**.

---

## 11. Output Ciphertext → Write to Shared Memory Buffer

After encryption, the TEE writes the **ciphertext (encrypted data)** into the shared memory buffer.  
This ciphertext is **safe to leave the TEE** because it’s no longer secret.

---

## 12. Kernel Trusted Driver Reads Buffer

The kernel driver copies the ciphertext from the shared memory buffer back to the Android side.  
**Plaintext never appears here — only ciphertext.**

---

## 13. Pass Ciphertext Back to KeyStore HAL

The **KeyStore HAL** receives the ciphertext.  
It may do some additional formatting or return it as-is to the requesting app.

---

## 14. Returns Ciphertext to App

The app finally receives the **encrypted data**.  
The app can **store or send** this ciphertext — it’s safe even if stolen.

---

## 15. App Stores Ciphertext in Normal Storage (Flash / File System)

The app saves the encrypted file or sends it over the network.  
Because it’s encrypted, **attackers can’t read it without access to the Knox Vault key**.

---

## 🌟 Key Takeaways from This Flow

- **Normal World vs Secure World** separation is the backbone.  
- **Keys never leave** the secure world.  
- **Integrity checks** happen before every crypto operation.  
- **Plaintext appears only** inside TEE memory.  
- **App always gets ciphertext, never the key.**

---
## How Knox Decrypt data 

<img width="1869" height="808" alt="Screenshot 2025-09-28 230721" src="https://github.com/user-attachments/assets/8807e473-80ae-418b-be30-a46e9fa1bf21" />

# 🔑 Decryption Flow 

## 1. App (Normal World)
Any normal Android app — e.g., banking, password manager, gallery — is running in the “normal” world of Android.

- The app has encrypted data (ciphertext) and needs it back as plaintext to display or process.
- The app does **not** decrypt on its own; it uses Android/Knox secure APIs.

## 2. Calls Android KeyStore / Knox Keystore HAL API
The app calls the KeyStore API or Knox HAL API.

- Sends:
  - Ciphertext (the encrypted data)
  - Key handle (a reference to the real key inside Knox Vault)
- The app **never sees the real key**.

## 3. Packages Ciphertext + Key Handle into Secure Request
- The KeyStore HAL wraps the ciphertext and key handle into a secure message.
- This message will travel from Android (Normal World) into the secure environment (TEE).

## 4. Kernel Trusted Driver (`/dev/qseecom` or `/dev/tzdev`)
- Acts as a secure tunnel between Android and the secure processor (TrustZone/TEE).
- Only trusted system services can use it; apps cannot access it directly.

## 5. Allocates Shared Memory Buffer
- Before data is sent to the TEE, the driver allocates a shared memory area.
- Buffer is protected and accessible by both Normal World and Secure World.
- **Ciphertext is copied here temporarily — the key stays secure in the TEE.**

## 6. Secure Monitor Call (SMC) → Switch CPU to TEE (Secure World)
- The driver sends an SMC instruction to the processor.
- CPU switches context from Normal World (Android) to Secure World (TEE).
- Now the processor executes code inside the TEE Trusted App.

## 7. TEE Trusted App (Keymaster / Knox)
- Inside the TEE lives the Knox Trusted App (Keymaster on Android).
- Small OS + app is isolated, signed, and protected — Android malware cannot change it.
- **All cryptographic operations happen here.**

## 8. Policy & Integrity Check (Verification Stage)
Before processing the ciphertext, the TEE checks:

- **Secure Boot Verified?**
  - Confirms device booted from trusted, signed boot chain.
  - Detects firmware tampering or replacement.
- **Tamper Sensors OK?**
  - Checks voltage, glitch, laser, and temperature sensors.
  - If abnormal, Knox can wipe keys or block operations.
- **Authorization Check:**
  - Confirms calling app is allowed to use the key handle.
  - Matches app UID/package signature with registered metadata.

> Only if all checks pass will Knox retrieve and use the decryption key.

## 9. Key Retrieval from Knox Vault (Secure Storage)
- TEE fetches the decryption key from Knox Vault.
- Key:
  - Lives only inside secure hardware storage.
  - Never leaves the TEE.
  - Can be revoked or wiped if tampering detected.

## 10. Decryption Operation (AES / RSA / ECC inside TEE Memory)
- Inside the TEE, ciphertext is decrypted using the secret key.
- Supported algorithms:
  - AES (symmetric decryption)
  - RSA / ECC (asymmetric decryption)
- Both key and plaintext stay inside secure memory.
- **Ciphertext → Plaintext**

## 11. Output Plaintext → Write to Shared Memory Buffer
- After decryption, plaintext is placed in the shared memory buffer.
- Carefully controlled; plaintext appears briefly.
- In some cases, plaintext is **not returned at all** — used directly in TEE (e.g., key unwrapping).

## 12. Kernel Trusted Driver Reads Buffer
- Driver reads the plaintext from shared memory.
- Only authorized KeyStore HAL can receive it.
- Plaintext is not visible to random processes or apps.

## 13. Pass Plaintext Back to KeyStore HAL
- KeyStore HAL receives plaintext.
- May:
  - Return plaintext to the requesting app.
  - Use it internally for another cryptographic operation (e.g., signing).

## 14. Returns Plaintext to App
- If policy allows, plaintext is returned to the app.
- Usually kept in **RAM only**.

## 15. App Uses Plaintext (Not Stored in Normal Storage)
- Best practice: use plaintext in memory and discard quickly.
- Storing plaintext in flash or external storage **defeats Knox security**.

---

# 🌟 Key Takeaways (Expanded)
- Normal World vs Secure World separation guarantees safety.
- Secure Boot + Tamper Sensors verify device integrity every time.
- Key Handles + Authorization ensure only the correct app can decrypt.
- **Keys Never Leave Secure Storage** — all crypto happens inside TEE.
- Plaintext appears briefly, only inside secure memory, and is usually not stored.
