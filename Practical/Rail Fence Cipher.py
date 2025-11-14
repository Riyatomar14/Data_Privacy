# Rail Fence Cipher - Encryption and Decryption

def encrypt_rail_fence(text, key):
    rail = ['' for _ in range(key)]
    direction_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)


def decrypt_rail_fence(cipher, key):
 
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0
 
    for _ in cipher:
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

   
    result = []
    row, col = 0, 0
    direction_down = True

    for _ in cipher:
        result.append(rail[row][col])

        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)
plaintext = "HELLOTHISISRAILFENCE"
key = 3

cipher = encrypt_rail_fence(plaintext, key)
print("Encrypted:", cipher)

decrypted = decrypt_rail_fence(cipher, key)
print("Decrypted:", decrypted)
