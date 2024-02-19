from Cryptodome.Cipher import AES
from PIL import Image


# Padding data by appending 0s to the end of the data
def pad(data):
    return data + b"\x00"*(16-len(data) % 16)


# Encrypt data using AES. ECB mode is used
def aes_ecb_encrypt(key, data):
    aes = AES.new(key, AES.MODE_ECB)
    new_data = aes.encrypt(data)
    return new_data


# Encrypt data using AES. CBC mode is used
# IV is defined as b'0000000000000000'
def aes_cbc_encrypt(key, data):
    aes = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    new_data = aes.encrypt(data)
    return new_data


def aes_ofb_encrypt(key, data):
    aes = AES.new(key, AES.MODE_OFB, iv=b'0000000000000000')
    new_data = aes.encrypt(data)
    return new_data


def aes_cfb_encrypt(key, data):
    aes = AES.new(key, AES.MODE_CFB, iv=b'0000000000000000')
    new_data = aes.encrypt(data)
    return new_data



def aes_ctr_encrypt(key, data):
    aes = AES.new(key, AES.MODE_CTR, nonce=b'00000000')
    new_data = aes.encrypt(data)
    return new_data


def encrypt_ECB(key, filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    en_data = aes_ecb_encrypt(key, pad(data))[:original]

    en_data = Image.frombytes("RGB", im.size, bytearray(en_data))
    en_data.save(filename + "_ecb.jpg", "JPEG")


def encrypt_CBC(key, filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    en_data = aes_cbc_encrypt(key, pad(data))[:original]

    en_data = Image.frombytes("RGB", im.size, bytearray(en_data))
    en_data.save(filename + "_cbc.jpg", "JPEG")


def encrypt_OFB(key, filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    en_data = aes_ofb_encrypt(key, pad(data))[:original]

    en_data = Image.frombytes("RGB", im.size, bytearray(en_data))
    en_data.save(filename + "_ofb.jpg", "JPEG")


def encrypt_CFB(key, filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    en_data = aes_cfb_encrypt(key, pad(data))[:original]

    en_data = Image.frombytes("RGB", im.size, bytearray(en_data))
    en_data.save(filename + "_cfb.jpg", "JPEG")

def encrypt_CTR(key, filename):
    im = Image.open(filename)
    data = im.convert("RGB").tobytes()
    original = len(data)
    en_data = aes_ctr_encrypt(key, pad(data))[:original]

    en_data = Image.frombytes("RGB", im.size, bytearray(en_data))
    en_data.save(filename + "_ctr.jpg", "JPEG")


key = b'1111111111111111'

encrypt_ECB(key, "1.png")
encrypt_ECB(key, "2.png")
encrypt_ECB(key, "3.png")
encrypt_ECB(key, "4.png")

encrypt_CBC(key, "1.png")
encrypt_CBC(key, "2.png")
encrypt_CBC(key, "3.png")
encrypt_CBC(key, "4.png")

encrypt_CTR(key, "1.png")
encrypt_CTR(key, "2.png")
encrypt_CTR(key, "3.png")
encrypt_CTR(key, "4.png")

encrypt_OFB(key, "1.png")
encrypt_OFB(key, "2.png")
encrypt_OFB(key, "3.png")
encrypt_OFB(key, "4.png")

encrypt_CFB(key, "1.png")
encrypt_CFB(key, "2.png")
encrypt_CFB(key, "3.png")
encrypt_CFB(key, "4.png")



