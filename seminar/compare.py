import time
from aes import aes_ecb_encrypt
from new import pad, enc, enc2
import threading

# timer to time the execution of the function


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

# function to compare two strings


file = open("input.txt", "r")
# data = file.read()
# file.close()

# read data as bytes
data = file.read().encode()
file.close()

key = b'9Q9qeuW1tgaCbjiX'

# @timer
# def test_aes_ecb_encrypt(data, key):
#     return aes_ecb_encrypt(key, pad(data))

# @timer
# def test_enc(data, key):
#     return enc(data, key)


# t1 = threading.Thread(target=timer(aes_ecb_encrypt), args=(key, pad(data))) #0.7299351692199707
t2 = threading.Thread(target=timer(enc), args=(data, key))
# t3 = threading.Thread(target=timer(enc2), args=(data, key))

# t1.start()
t2.start()
# t3.start()

# t1.join()
t2.join()
# t3.join()