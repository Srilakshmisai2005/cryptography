from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
key = get_random_bytes(16)
iv = get_random_bytes(16)
plaintext = b"This is a sample plaintext."
block_size = AES.block_size
padded_plaintext = pad(plaintext, block_size)
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_cipher.encrypt(padded_plaintext)
cbc_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
cbc_ciphertext = cbc_cipher.encrypt(padded_plaintext)
cfb_cipher = AES.new(key, AES.MODE_CFB, iv=iv)
cfb_ciphertext = cfb_cipher.encrypt(padded_plaintext)
ecb_decipher = AES.new(key, AES.MODE_ECB)
ecb_decrypted = unpad(ecb_decipher.decrypt(ecb_ciphertext), block_size)
cbc_decipher = AES.new(key, AES.MODE_CBC, iv=iv)
cbc_decrypted = unpad(cbc_decipher.decrypt(cbc_ciphertext), block_size)
cfb_decipher = AES.new(key, AES.MODE_CFB, iv=iv)
cfb_decrypted = unpad(cfb_decipher.decrypt(cfb_ciphertext), block_size)
print("Original plaintext:", plaintext)
print("ECB decrypted:", ecb_decrypted.decode('utf-8'))
print("CBC decrypted:", cbc_decrypted.decode('utf-8'))
print("CFB decrypted:", cfb_decrypted.decode('utf-8'))
