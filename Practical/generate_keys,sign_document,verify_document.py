FIRST INSTALL --> pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import os

# ------------------------------------------------------------
# 1. GENERATE RSA KEY PAIR
# ------------------------------------------------------------

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Save private key
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    public_key = private_key.public_key()
    with open("public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    
    print("[✔] Keys generated: private_key.pem , public_key.pem")


# ------------------------------------------------------------
# 2. SIGN DOCUMENT USING PRIVATE KEY
# ------------------------------------------------------------

def sign_document():
    # Load private key
    private_key = serialization.load_pem_private_key(
        open("private_key.pem", "rb").read(),
        password=None
    )

    # Read document
    document = open("document.txt", "rb").read()

    # Create signature
    signature = private_key.sign(
        document,
        padding.PSS( #randomness add 
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Save signature
    with open("document.sig", "wb") as f:
        f.write(signature)
    
    print("[✔] Document signed → document.sig created!")


# ------------------------------------------------------------
# 3. VERIFY DOCUMENT USING PUBLIC KEY
# ------------------------------------------------------------

def verify_document():
    # Load public key
    public_key = serialization.load_pem_public_key(
        open("public_key.pem", "rb").read()
    )

    # Load document + signature
    document = open("document.txt", "rb").read()
    signature = open("document.sig", "rb").read()

    try:
        public_key.verify(
            signature,
            document,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("[✔] Signature VALID → Document is authentic.")
    except Exception:
        print("[✘] Signature INVALID → Document altered or fake!")


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

# Create a sample document if not exists
if not os.path.exists("document.txt"):
    with open("document.txt", "w") as f:
        f.write("This is a confidential message.\nSigned using RSA digital signature.")

generate_keys()
sign_document()
verify_document()
