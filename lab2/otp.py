initial_plain_text = "attack at dawn"
initial_cipher_text_in_hex = "09e1c5f70a65ac519458e7e53f36"

required_plain_text = "attack at dusk"

otp_key = bin(int(initial_plain_text.encode().hex(), 16) ^ int(initial_cipher_text_in_hex, 16))[2:]
print("OTP key is: ", otp_key)

required_cipher_text_in_hex = hex(int(required_plain_text.encode().hex(), 16) ^ int(otp_key, 2))[2:]
print("Required cipher text is: ", required_cipher_text_in_hex)
