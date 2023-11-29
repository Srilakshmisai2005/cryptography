def encrypt(plaintext, key_stream):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = key_stream[i % len(key_stream)]
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key_stream):
    plaintext = ""
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key_stream[i % len(key_stream)]
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    plaintext = "send more money"
    key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    encrypted_text = encrypt(plaintext, key_stream)
    print("Encrypted ciphertext:")
    print(encrypted_text)

   
    decrypted_text = "cash not needed"
    key_stream_found = []
    for i in range(len(decrypted_text)):
        shift = (ord(decrypted_text[i]) - ord(encrypted_text[i])) % 26
        key_stream_found.append(shift)
    
    print("\nFound key stream:")
    print(key_stream_found)
