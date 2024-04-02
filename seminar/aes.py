from Cryptodome.Cipher import AES

def aes_ecb_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    new_data = aes.encrypt(data)
    return new_data

