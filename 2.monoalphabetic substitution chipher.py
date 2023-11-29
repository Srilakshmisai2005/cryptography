def monoalphabetic_substitution(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            encrypted_char = key[index] if char.islower() else key[index].upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

plaintext = input("Enter the text: ")
key = input("Enter the substitution key (26 unique letters): ")

if len(key) != 26 or not all(char.isalpha() and char.islower() for char in key):
    print("Key should be 26 unique lowercase letters.")
else:
    encrypted_text = monoalphabetic_substitution(plaintext, key)
    print("Encrypted:", encrypted_text)
