"""Challenge Overview
Convert a phrase into a URL-friendly slug.

Prompt the user for a phrase or title.
Lowercase the text and remove punctuation/symbols (keep letters, numbers, and spaces).
Replace spaces with hyphens and collapse multiple hyphens.
Handle empty or all-symbol input with a friendly message.
Examples

Input: "Summer Sale 2026!!!"
Output: "summer-sale-2026"
Punctuation is removed and spaces become hyphens.
    """

'''
1. ask the user to enter a phrase
2. set the phrase to lower case
3. remove any unique characters
4. replace the spaces with -
5. print the new phrase
'''
import string
def url_slug_builder():
    phrase = input("Please enter a phrase: ")#get the phrase from the user

    while phrase == "":#check if the user entered an empty string
        print("You must enter a phrase. Please try again.")
        phrase = input("Please enter a phrase: ")

    phrase = phrase.lower()#set the phrase to lower case
    phrase = phrase.strip()#remove any leading or trailing whitespace

    special_chars_string = string.punctuation
    special_chars_list = list(special_chars_string)#create a list of all the special characters using the string module
    for i in special_chars_list:#remove any unique characters
        phrase = phrase.replace(i, "")
    if phrase == '': #check if the phrase is empty after removing punctuation
        print("Your phrase must contain at least one letter or number. Please try again.")
        return url_slug_builder()

    phrase = phrase.replace(" ", "-")#replace the spaces with -

    x = len(phrase)-1
    for i in range(x, 0, -1):#collapse multiple hyphens
        if phrase[i]=="-" and phrase[i-1] == "-":
            phrase = phrase[:i] + phrase[i+1:]
    print(phrase)
    print("Your URL slug is:", phrase)

url_slug_builder()
