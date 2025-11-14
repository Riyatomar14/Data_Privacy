# PROGRAM TO CONVERT STRING AND RETURN HEXADECIMAL STRING
import hashlib

def sha256_hash(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
print(sha256_hash("mySecretPassword"))

