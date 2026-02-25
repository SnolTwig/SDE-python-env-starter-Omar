
import string
def generate_acronym():
    acronym = ""
    phrase = input("Enter a phrase to generate its acronym: ")#get user input

    if phrase == "":#check for empty input
        print("Please enter a valid phrase.")
        return generate_acronym()


    special_chars_string = string.punctuation
    special_chars_list = list(special_chars_string)
    for i in special_chars_list: #remove punctuation and spaces from the word
        phrase = phrase.replace(i, " ")

    phrase_list = phrase.split()#split the phrase into words

    if len(phrase_list) <= 1:#check if there is more than one word
        print("Please enter more than one word.")
        return generate_acronym()

    for word in phrase_list:#get the first letter of each word
        acronym += word[0]

    acronym = acronym.upper()#convert the acronym to uppercase
    print(acronym)#print the acronym

generate_acronym()
