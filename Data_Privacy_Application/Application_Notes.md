# Data Privacy Primitives and Applications
## 1. Key Exchange Primitives
| Keyword                                        | Real-Time Use Cases                                                                             | How It’s Actually Used                                                                                                                                                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Diffie–Hellman (DH / ECDH)**                 | HTTPS (when you open `https://bank.com`), Signal/WhatsApp chats, OpenVPN, SSH login             | When you connect to your bank’s site, your browser and the bank secretly agree on a shared key (like a secret handshake). Hackers watching can’t figure out the key even though they see the exchange.       |
| **PAKE (Password Authenticated Key Exchange)** | WPA3 Wi-Fi login, Apple iCloud Keychain sync, Banking PIN login                                 | When you enter your Wi-Fi password for WPA3, it proves to the router that you know the password **without sending it**. So hackers near your Wi-Fi can’t steal the password even if they capture the signal. |
| **Post-Quantum Key Exchange**                  | Chrome experiments with Kyber, Cloudflare PQ encryption, IBM VPN trials, Microsoft PQC adoption | Companies are testing PQC so that **future quantum computers** won’t decrypt today’s secure messages. Example: Cloudflare already protects some TLS connections with quantum-safe keys.                      |

## 2. Signature Schemes
| Keyword                     | Real-Time Use Cases                                                          | How It’s Actually Used                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Digital Signature**       | DocuSign contracts, Git commit signing, App store apps, SSL/TLS certificates | When you download an app from the Play Store, it’s digitally signed. Your phone checks the signature to confirm it really came from Google/Apple and hasn’t been tampered with. |
| **Group Signature**         | GDPR compliance logs, IoT consortium networks                                | Example: A hospital system signs medical logs using group signatures. Auditors know “someone from the hospital signed it,” but not which specific doctor.                       |
| **Ring Signature**          | Monero cryptocurrency, SecureDrop whistleblower platform                     | In Monero, every transaction looks like it could come from many possible senders. Outsiders can’t tell who actually sent it.                                                    |
| **Blind Signature**         | E-cash pilots, Transit cards, Privacy-preserving voting                      | Example: In e-voting, the election authority signs your ballot **without seeing it**, so your vote remains secret but still valid.                                              |
| **Threshold Signature**     | BitGo multi-party crypto wallets, DAO governance, Nuclear launch protocols   | Example: A crypto company stores customer funds in a wallet that needs **3 of 5 executives’ keys** to approve a transfer, so no single person can steal funds.                  |
| **Post-Quantum Signatures** | IBM quantum-safe blockchain demos, Cloudflare DNSSEC PQ tests                | Ensures signatures remain valid even if quantum computers emerge. Example: Cloudflare tests PQ signatures on internet infrastructure like DNSSEC.                               |

## 3. Mixing Protocols
| Keyword                | Real-Time Use Cases                          | How It’s Actually Used                                                                                                                                          |
| ---------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mixers / Tumblers**  | Tornado Cash (Ethereum), ChipMixer (Bitcoin) | If Alice sends 1 BTC to Bob, normally blockchain shows it clearly. With a mixer, Alice’s BTC is shuffled with many others before reaching Bob, hiding the link. |
| **CoinJoin**           | Wasabi Wallet, JoinMarket                    | Several people combine their payments into one giant transaction. Outsiders see money moving, but can’t match “who paid whom.”                                  |
| **CoinSwap**           | Bitcoin swaps, Lightning Network             | Alice swaps her Bitcoin with Bob’s coins without outsiders knowing. To the blockchain, it looks like unrelated normal transactions.                             |
| **CoinShuffle**        | Dash PrivateSend                             | Adds randomness on top of CoinJoin, making the pattern of senders/receivers harder to trace.                                                                    |
| **Dandelion Protocol** | Grin, MimbleWimble                           | Instead of broadcasting a transaction directly, it passes through several random nodes first. This hides Alice’s IP so no one knows where it originated.        |

## 4. Conditional Payments & Proofs
| Keyword                                      | Real-Time Use Cases                         | How It’s Actually Used                                                                                                                       |
| -------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **ZKCP (Zero-Knowledge Contingent Payment)** | Bitcoin trustless payments                  | Alice buys a software key from Bob. Payment is released **only if** Bob gives the correct key. No middleman, no scams.                       |
| **zk-SNARKs**                                | Zcash private payments, Ethereum zk-rollups | In Zcash, you can prove you have enough balance to pay Bob **without revealing your balance or the transaction amount**.                     |
| **zk-STARKs**                                | StarkNet rollups, ImmutableX NFT platform   | Used to bundle thousands of Ethereum transactions into one proof for speed, while hiding sensitive data.                                     |
| **Bulletproofs**                             | Monero transactions, DeFi privacy           | Hides transaction amounts but proves they add up correctly (e.g., no one created fake money).                                                |
| **zk-Rollups**                               | zkSync, Polygon zkEVM                       | Thousands of transactions are compressed into one proof, reducing fees and keeping privacy.                                                  |
| **Fair Exchange Protocols**                  | Atomic swaps, Cross-chain bridges           | Alice trades Bitcoin for Bob’s Ethereum directly. The protocol ensures **either both get the coins or neither does** — no cheating possible. |

## 5. Pseudorandom Functions (PRFs)
| Keyword  | Real-Time Use Cases                                         | How It’s Actually Used                                                                                                     |
| -------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **PRF**  | TLS session keys, AWS tokens                                | When you log in to Gmail, TLS uses PRFs to generate secure keys so each session is unpredictable to outsiders.             |
| **OPRF** | iCloud Private Relay, OPAQUE password logins                | Example: Apple iCloud Relay uses OPRF so Apple can’t see which websites you visit, but still helps route traffic securely. |
| **VRF**  | Algorand blockchain leader election, Chainlink random draws | In Algorand, VRFs fairly select who creates the next block. Everyone can verify the lottery was random.                    |

## 6. Encryption Approaches
| Keyword                        | Real-Time Use Cases                             | How It’s Actually Used                                                                                                          |
| ------------------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Symmetric Encryption**       | WhatsApp end-to-end encryption (AES), BitLocker | Your WhatsApp messages are encrypted with a shared secret key known only to you and your contact.                               |
| **Asymmetric Encryption**      | RSA/ECC in HTTPS, PGP email, Blockchain wallets | When you send an email with PGP, you use the recipient’s public key to encrypt. Only their private key can unlock it.           |
| **Homomorphic Encryption**     | Secure medical research, Microsoft SEAL         | Hospitals encrypt patient data before sending to cloud researchers, who can still run computations without seeing the raw data. |
| **Attribute-Based Encryption** | Hospital electronic records                     | A nurse with “Emergency Role” can open certain files, while others can’t — access is tied to roles, not just passwords.         |
| **Functional Encryption**      | Cloud AI analytics                              | A company can run analytics on encrypted sales data but can only decrypt **the average sales**, not individual records.         |
| **Identity-Based Encryption**  | Secure enterprise emails                        | Your email ID (`alice@company.com`) acts as a public key, making encryption simpler without distributing separate certificates. |
| **Searchable Encryption**      | ProtonDrive, CipherCloud                        | Lets you search “Invoices 2024” inside encrypted files stored in the cloud **without decrypting them first**.                   |

## 7. Anonymity Techniques (5 Levels)
| Level                    | Real-Time Use Cases         | How It’s Actually Used                                                                                             |
| ------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **1. Network-Level**     | Tor Browser, VPNs, I2P      | When you browse with Tor, your request goes through multiple relays, hiding your IP and location from the website. |
| **2. Transaction-Level** | Monero, Zcash, Tornado Cash | In Monero, transaction graphs are obfuscated, so no one can link payments between people.                          |
| **3. Signature-Level**   | Ring & Group Signatures     | In SecureDrop, whistleblowers can sign files without revealing their identity.                                     |
| **4. Function-Level**    | OPRF, PSI for ads           | Facebook can check if you’re in a target audience set **without learning your full personal data**.                |
| **5. PETs**              | OnionShare, MPC, ZK proofs  | OnionShare lets you send files via Tor where **only the recipient** can download, without servers knowing.         |

## 8. Confidentiality Approaches
| Area                          | Real-Time Use Cases             | How It’s Actually Used                                                                                       |
| ----------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Data-in-Transit**           | HTTPS, TLS, QUIC                | When you shop online, your card details are encrypted while traveling from your browser to the store server. |
| **Data-at-Rest**              | FileVault, BitLocker            | If someone steals your laptop, encrypted hard drive ensures files can’t be opened without password.          |
| **Data-in-Use**               | Intel SGX, AMD SEV              | Cloud providers can run AI models on your encrypted data inside secure CPU hardware enclaves.                |
| **Secure Cloud Storage**      | ProtonDrive, Tresorit           | Your files are encrypted **before upload**, so even the cloud provider cannot read them.                     |
| **Confidential Transactions** | Monero blockchain               | Transaction amounts are hidden but still provably valid (no double-spend).                                   |
| **Differential Privacy**      | Apple iOS keyboard, Google Maps | Apple adds “noise” to typing data so they can improve autocorrect without knowing your exact words.          |
| **Federated Learning**        | Google Gboard, Healthcare AI    | Your phone trains an AI locally and only sends model updates, not raw text, to the central server.           |

## 9. Blockchain & DLT Applications
| Area                         | Real-Time Use Cases                      | How It’s Actually Used                                                                                         |
| ---------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Financial Privacy**        | Monero, Zcash                            | People can pay privately so that outsiders (governments, trackers) can’t trace amounts or identities.          |
| **Decentralized Identity**   | Microsoft Entra Verified ID, W3C DIDs    | Example: You prove your age to a bar using a digital credential without showing your full ID.                  |
| **Medical Records**          | Estonia e-Health, Guardtime blockchain   | Estonia secures patient health data so only doctors with permission can view. Any tampering is detectable.     |
| **E-Voting & Governance**    | Swiss Post blockchain voting, DAO voting | Voters can prove their vote is counted correctly without revealing who they voted for.                         |
| **Supply Chain**             | IBM Food Trust, VeChain                  | Walmart tracks mangoes on blockchain: customers can scan QR code to see farm-to-store journey.                 |
| **Web3 / DAO / NFT Privacy** | zkSync, Aztec protocol                   | NFT trades can be private — the buyer/seller identities and amounts are hidden while the trade is still valid. |
| **Selective Disclosure**     | zk-KYC (crypto compliance)               | You can prove you’re over 18 (KYC) to use a DeFi app **without revealing your name or passport**.              |
