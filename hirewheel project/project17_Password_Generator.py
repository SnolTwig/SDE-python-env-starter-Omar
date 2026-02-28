"""1. import random
2. import string
3. ask user for length of password and check that its a string greater than or equal to 4
4. ask user what types of characters to include(uppercase, lowercase, digits, and/or symbols) set equal to included_char
5. convert included_char to list
6. initializes character_list
7. if uppercase is in the list add string.ascii_uppercase to character_list
8. if lowercase is in the list add string.ascii_lowercase to character_list
9. if symbols is in the list add string.punctuation to character_list
10. if numbers is in the list add string.digits to character_list
11. convert character_list to list
12. password =  ''.join(random.sample(character_list, length))
13. print out password

Generate a random password with user-specified length and character types.

Prompt the user for the desired password length (minimum 4).
Ask which character types to include: uppercase, lowercase, digits, and/or symbols.
Build a character pool from the selected types and randomly assemble the password.
Display the generated password and confirm it meets the requested criteria.
Examples

Input: length=12, types=uppercase+lowercase+digits
Output: "Generated password: aB3kR9mW2xLp"
A 12-character password assembled from letters and digits.
"""

import random
import string
def password_generator():
    length = input("Enter the desired length of your password (must be at least 4 characters): ")
    while not length.isdigit() or int(length) < 4:
        print("Invalid input. Please enter a number greater than or equal to 4.")
        length = input("Enter the desired length of your password (must be at least 4 characters): ")
    length = int(length)

    included_char = input("Which types of characters would you like to include in your password? (uppercase, lowercase, digits, symbols) Separate with commas: ")
    included_char_list = [char.strip().lower() for char in included_char.split(",")]

    character_list = ""
    if "uppercase" in included_char_list:
        character_list += string.ascii_uppercase
    if "lowercase" in included_char_list:
        character_list += string.ascii_lowercase
    if "digits" in included_char_list:
        character_list += string.digits
    if "symbols" in included_char_list:
        character_list += string.punctuation

    if not character_list:
        print("No valid character types selected. Please select at least one type.")
        return

    password = ''.join(random.sample(character_list, length))
    print(f"Generated password: {password}")
