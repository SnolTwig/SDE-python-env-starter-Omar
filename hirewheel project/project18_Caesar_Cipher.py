import string

def caesar_cipher():
    encrypt = input("Would you like to encrypt or decrypt a message? (enter 'encrypt' or 'decrypt'): ").lower()
    while encrypt not in ['encrypt', 'decrypt']:
        encrypt = input("Invalid input. Please enter 'encrypt' or 'decrypt': ").lower()

    mesage = input("Enter the message to encrypt: ").lower()

    shift = int(input("Enter the shift value: "))
    while shift < 0 or shift > 26:
        shift = int(input("Shift value must be between 0 and 26. try again: "))

    encrypted_message = ""
    if encrypt == 'encrypt':
        for char in mesage:
            if char in string.ascii_lowercase:
                shifted_index = (string.ascii_lowercase.index(char) + shift) % 26
                encrypted_message += string.ascii_lowercase[shifted_index]
            else:
                encrypted_message += char
    else:
        for char in mesage:
            if char in string.ascii_lowercase:
                shifted_index = (string.ascii_lowercase.index(char) - shift) % 26
                encrypted_message += string.ascii_lowercase[shifted_index]
            else:
                encrypted_message += char

    print("Encrypted message:", encrypted_message)

caesar_cipher()
