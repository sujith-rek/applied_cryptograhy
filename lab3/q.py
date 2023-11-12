# Q. Block cipher ‘Mode of Operation’: ECB and CBC
# As discussed, the ECB mode of operation leaves too many clues in the ciphertext
# for an attacker due to repetitive pattern in the input. Take an image data and
# demonstrate the same considering DES or AES as your underlying block cipher.
# Next encrypt the same image using CBC mode of operation and justify why such
# repetitions are not visible. You can use any programming language of your
# choice

# https://www.quora.com/How-do-I-encrypt-and-decrypt-an-image-file-using-ECB-CBC-AES-encryption-or-something-like-this-in-python-using-a-program

from Cryptodome.Cipher import AES
from PIL import Image
import PIL
import os

# ECB mode
# files are 1.png, 2.png, 3.png

# 1.png
# im = Image.open('1.png')
# im = im.convert('RGB')
# im.save('1.jpg')
# im.close()

# ECB mode

key = b'Sixteen byte key'


cipher = AES.new(key, AES.MODE_ECB)

file_size = os.path.getsize('1.jpg').to_bytes(16, byteorder='big')


with open('1.jpg', 'rb') as f:
    with open('1_ecb.jpg', 'wb') as g:
        while True:
            chunk = f.read(16)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)
            enc = cipher.encrypt(chunk)
            g.write(enc)

        f.close()
        g.close()


im = Image.open('1_ecb.jpg')
im = im.convert('RGB')
im.save('1_ecb.jpg')
im.close()
    


    

    
