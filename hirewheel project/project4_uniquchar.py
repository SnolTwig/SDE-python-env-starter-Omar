'''
take a string from the user then remove all special characters leaving only the letters. then sort through the string to see if it has any duplicate characters  if they do then return false
'''
import string
def unique_char():
    user_input = input("Please enter a string: ")#take user input
    if user_input == "":#check for empty input
        print("You must enter a string. Please try again.")
        unique_char()
        return

    try:#check if the input is a number and force the user to enter a string
        int(user_input)
        print("That is not a valid string. Please try again.")
        unique_char()
        return

    except ValueError:#process the string
        user_input = user_input.lower()

        special_chars_string = string.punctuation
        special_chars_list = list(special_chars_string)
        for i in special_chars_list:#remove punctuation and spaces from the word
            user_input = user_input.replace(i, "")
        user_input = user_input.replace(" ", "")

        if user_input == '': #check if the word is empty after removing punctuation
            print("The string does not have all unique characters.")
            return False
        
        ui_list = list(user_input)#convert the string to a list for easier comparison
        unique = True
        for i in range(len(ui_list)):#check for duplicate characters
            for j in range(i+1, len(ui_list)):
                if ui_list[i] == ui_list[j]:
                    unique = False
                    break

        if unique == False:#print the result
           print("The string does not have all unique characters.")
           return False
        else:
            print("The string has all unique characters.")
            return True
unique_char()
