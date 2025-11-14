# Rail Fence Cipher - Encryption and Decryption

def encrypt_rail_fence(text, key):
    rail = ['' for _ in range(key)]
    row, direction = 0, 1

    for ch in text:
        rail[row] += ch
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    return ''.join(rail)


def decrypt_rail_fence(cipher, key):
    # Step 1: Mark rail pattern
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]
    row, direction = 0, 1

    for col in range(len(cipher)):
        rail[row][col] = '*'
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    # Step 2: Fill rail with letters
    index = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*':
                rail[r][c] = cipher[index]
                index += 1

    # Step 3: Read zigzag to decrypt
    result = []
    row, direction = 0, 1
    for col in range(len(cipher)):
        result.append(rail[row][col])
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    return ''.join(result)


# -------- USER INPUT --------
plaintext = input("Enter text: ")
key = int(input("Enter key: "))

cipher = encrypt_rail_fence(plaintext, key)
print("Encrypted:", cipher)

decrypted = decrypt_rail_fence(cipher, key)
print("Decrypted:", decrypted)
