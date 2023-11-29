def decrypt_simple_substitution(ciphertext, key):
    decryption = ""

    for char in ciphertext:
        if char.isalpha():
            decrypted_char = key[char]
            decryption += decrypted_char
        else:
            decryption += char

    return decryption

ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 " \
             "(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* " \
             ";4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 " \
             "(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
             
hints = {
    '†': 'E',  
    '4': 'T',  
    '8': 'H',  
    '†': 'E',  
    '3': 'R',  
    '1': 'A',  
    ';': 'N',  
    '6': 'I',  
    '5': 'S',  
    '0': 'O',  
    '—': 'F',  
    ':': 'U',  
    ']': 'L',  
    '(': 'W',  
    '(': 'W',  
    ')': 'Y',  
    '?': 'G',  
}
decryption_key = {k: v for k, v in hints.items() if k.isalpha()}
decrypted_message = decrypt_simple_substitution(ciphertext, decryption_key)

print("Decrypted Message:")
print(decrypted_message)


