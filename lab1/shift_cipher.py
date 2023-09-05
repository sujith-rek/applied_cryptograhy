import index_of_coincidence

def break_shift(cipher):

    # Calculate the index of coincidence for each shift
    shifts = {}
    for shift in range(26):
        shifted_text = ''.join([chr((ord(c) - 65 - shift) % 26 + 65) for c in cipher])
        shifts[shift] = index_of_coincidence.index_of_coincidence(shifted_text)

    # Find the shift with the highest index of coincidence
    max_ic = max(shifts.values())
    for shift in shifts:
        if shifts[shift] == max_ic:
            return shift
    


cipher = input('Enter the cipher text: ')
shift = break_shift(cipher)
print('The shift is', shift)
print('The plain text is', ''.join([chr((ord(c) - 65 - shift) % 26 + 65) for c in cipher]))

