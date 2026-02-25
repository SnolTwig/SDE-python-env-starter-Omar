'''
Done
'''
import string


def check_palidrome():
    word = input("please type the word you want to check: ")
    palindrome = True
    while word == "": #if the user enters nothing
        print("You must enter a word")
        word = input("please type the word you want to check: ")
    try:# check if the input is a number and force the user to enter a string
        int(word)
        print("That not a string, please try again")
        check_palidrome()
    except ValueError:
        word = word.lower() #convert the word to lower case to avoid case sensitivity
        special_chars_string = string.punctuation
        special_chars_list = list(special_chars_string)
        for i in special_chars_list: #remove punctuation and spaces from the word
            word = word.replace(i, "")
        if word == '': #check if the word is empty after removing punctuation
            palindrome = False

        for i in range(len(word)): #check if the word is a palindrome
            if word[i]!=word[len(word)-i-1]:
                palindrome = False
                break

        if palindrome == True:#print the result
            print("Your word is a palindrome")
        else:
            print("Your word is not a palindrome")
check_palidrome()
