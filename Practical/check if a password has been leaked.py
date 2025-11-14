# input file - as users.txt

alice,Password123
bob,123456
charlie,my-secret-pass



import hashlib
import requests

def sha1_hash(password: str) -> str:
    """Return the SHA-1 hash of a password in uppercase hexadecimal."""
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def check_pwned_password(password: str) -> int:
    """
    Checks password against Have I Been Pwned API.
    Returns: number of times it appears in breaches (0 = not found).
    """
    # Hash password
    sha1 = sha1_hash(password)
    prefix = sha1[:5]
    suffix = sha1[5:]

    # HIBP API range endpoint
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    # Query API
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"API error: {response.status_code}")

    # The response contains many suffixes and counts
    hashes = (line.split(':') for line in response.text.splitlines())

    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)

    return 0  # Not found


def check_password_file(filename: str):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "," not in line:
                continue

            username, password = line.split(",", 1)
            username = username.strip()
            password = password.strip()

            count = check_pwned_password(password)

            if count > 0:
                print(f"[LEAKED]  User: {username} | Password found {count} times!")
            else:
                print(f"[SAFE]    User: {username} | Password not found.")
            

if __name__ == "__main__":
    check_password_file("users.txt")
