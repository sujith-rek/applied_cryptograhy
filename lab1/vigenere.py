import index_of_coincidence
import kaisiski_test
import re

def shift_cipher(cipher, shift):
    plain_text = ''.join([chr((ord(c) - 65 - shift) % 26 + 65) for c in cipher])
    return plain_text

def break_vigenere(cipher):

    cipher = cipher.upper()
    cipher = re.sub(r'[^A-Z]', '', cipher)

    # Calculate the key length
    key_length = kaisiski_test.kaisiski_test(cipher)
  
    # make another subbgrop for chars of same index from cipher_groups
    cipher_subgroups = []
    for i in range(key_length):
        sub_str = ''
        for j in range(len(cipher)):
            if j % key_length == i:
                sub_str += cipher[j]

        cipher_subgroups.append(sub_str)


    ioc = []
    for i in range(key_length):
        individual_shifts = {}
        for j in range(26):
            individual_shifts[j] = index_of_coincidence.index_of_coincidence(
                shift_cipher(cipher_subgroups[i], j)
            )
        
        min_diff = min(abs(individual_shifts[shift] - 0.065) for shift in individual_shifts)
        for shift in individual_shifts:
            if abs(individual_shifts[shift] - 0.065) == min_diff:
                ioc.append(shift)
                break
    
    key = ''.join([chr(i + 65) for i in ioc])

    print('The key is', key)

    plain_text = ''.join([chr((ord(c) - 65 - ioc[i % key_length]) % 26 + 65) for i, c in enumerate(cipher)])

    return plain_text


cipher = input('Enter the cipher text: ')
plain_text = break_vigenere(cipher)
print('The plain text is', plain_text)
