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
    length = input("Enter the desired length of your password (must be at least 4 characters): ")#ask user for length of password
    while not length.isdigit() or int(length) < 4:#check that its a string greater than or equal to 4 and is a digit
        length = input("Invalid input. Please enter a number greater than or equal to 4. try again: ")#reask user for length of password
    length = int(length)

    included_char = input("Which types of characters would you like to include in your password? (uppercase, lowercase, digits, symbols) Separate with commas: ")#ask the user for what types of characters to include

    included_char = included_char.lower().strip().split(",")#convert included_char to list and remove any extra spaces and convert to lowercase
    included_char_list = []#initialize included_char_list to store valid character types

    for i in range(len(included_char)):#check that each character type is valid and if not ask the user to enter a valid character type
        if included_char[i].strip() not in ["uppercase", "lowercase", "digits", "symbols"]:
            new_char = input(f"'{included_char[i]}' is not a valid character type. Please enter a valid character type (uppercase, lowercase, digits, symbols): ")
            new_char = new_char.lower().strip()
            included_char[i] = new_char
        included_char_list.append(included_char[i].strip())


    character_list = ""#initialize character_list to store the characters that will be used to generate the password
    if "uppercase" in included_char_list:#adds uppercase letters to the list of characters to be used in the password
        character_list += string.ascii_uppercase
    if "lowercase" in included_char_list:#adds lowercase letters to the list of characters to be used in the password
        character_list += string.ascii_lowercase
    if "digits" in included_char_list:#adds numbers letters to the list of characters to be used in the password
        character_list += string.digits
    if "symbols" in included_char_list:#adds symbols letters to the list of characters to be used in the password
        character_list += string.punctuation

    password = ''.join(random.sample(character_list, length))#generate a random password by sampling characters from the character_list and joining them together
    print(f"Generated password: {password}")#print out the generated password

password_generator()
