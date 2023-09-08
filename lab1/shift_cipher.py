from index_of_coincidence import index_of_coincidence
import re

def break_shift(cipher):

    # Case convert and filter the cipher text
    cipher = cipher.upper()
    cipher = re.sub(r'[^A-Z]', '', cipher)

    # Calculate the index of coincidence for each shift
    shifts = {}
    for shift in range(26):
        shifted_text = ''.join([
            chr((ord(c) - 65 - shift) % 26 + 65) for c in cipher
        ])

        shifts[shift] = index_of_coincidence(shifted_text)

    # Find the shift with the minimum difference from 0.065
    min_diff = min(abs(shifts[shift] - 0.065) for shift in shifts)
    
    # Return the shift with the minimum difference
    for shift in shifts:
        if abs(shifts[shift] - 0.065) == min_diff:
            return shift
    


cipher = input('Enter the cipher text: ')
shift = break_shift(cipher)
print('The shift is', shift)
print('The plain text is', ''.join([chr((ord(c) - 65 - shift) % 26 + 65) for c in cipher]))

