from Cryptodome.Cipher import AES
from PIL import Image


# Padding data by appending 0s to the end of the data
def pad(data):
    return data + b"\x00"*(16-len(data) % 16)


# Convert data to RGB format
def convert_to_RGB(data):
    r, g, b = tuple(
        map(lambda d: [data[i] for i in range(0, len(data)) if i % 3 == d], [0, 1, 2]))
    pixels = tuple(zip(r, g, b))
    return pixels


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


key = b'1111111111111111'

encrypt_ECB(key, "1.png")
encrypt_ECB(key, "2.png")
encrypt_ECB(key, "3.png")

encrypt_CBC(key, "1.png")
encrypt_CBC(key, "2.png")
encrypt_CBC(key, "3.png")
