# 1.1
def caesar_cipher(message, shift, encrypt=True):
    result = ""
    for char in message:
        if 32 <= ord(char) <= 126:
            if encrypt:
                new_char = chr((ord(char) - 32 + shift) % 95 + 32)
            else:
                new_char = chr((ord(char) - 32 - shift) % 95 + 32)

            result += new_char
        else:
            result += char

    return result

# Example usage:
message_to_encrypt = "Hello, World!"
shift_amount = 3
encrypted_message = caesar_cipher(message_to_encrypt, shift_amount, encrypt=True)
decrypted_message = caesar_cipher(encrypted_message, shift_amount, encrypt=False)

print("Original Message:", message_to_encrypt)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

# 1.2
def vigenere_cipher(message, keyword, encrypt=True):
    result = ""
    keyword = keyword * (len(message) // len(keyword)) + keyword[:len(message) % len(keyword)]

    for i in range(len(message)):
        char = message[i]
        if 32 <= ord(char) <= 126:
            if encrypt:
                shift = ord(keyword[i]) - 32
                new_char = chr((ord(char) - 32 + shift) % 95 + 32)
            else:
                shift = ord(keyword[i]) - 32
                new_char = chr((ord(char) - 32 - shift) % 95 + 32)

            result += new_char
        else:
            result += char

    return result

# Example usage:
message_to_encrypt = "Hello, World!"
keyword = "KEY"
encrypted_message = vigenere_cipher(message_to_encrypt, keyword, encrypt=True)
decrypted_message = vigenere_cipher(encrypted_message, keyword, encrypt=False)

print("Original Message:", message_to_encrypt)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)

