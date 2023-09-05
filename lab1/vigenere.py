import index_of_coincidence
import kaisiski_test

def break_vigenere(cipher):

    # Find the key length
    # key_length = kaisiski_test.kaisiski_test(cipher)
    # print('The key length is', key_length)
    key_length = 8

    # we will break the cipher into substrings of length key_length
    # and then 
    key = ''

    print('The key is', key)

    # Decrypt the cipher
    plain_text = ''
    for i in range(len(cipher)):
        plain_text += chr((ord(cipher[i]) - 65 - ord(key[i % key_length]) + 65) % 26 + 65)
    return plain_text


cipher = input('Enter the cipher text: ')
plain_text = break_vigenere(cipher)
print('The plain text is', plain_text)
