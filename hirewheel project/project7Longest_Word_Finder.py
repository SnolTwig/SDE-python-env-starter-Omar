
import string
def longest_word():
    sent = input("Enter a sentence: ")

    while sent == "" or sent.isspace(): #if the user enters nothing or only whitespace
        print("You must enter a sentence")
        sent = input("Enter a sentence: ")

    special_chars_string = string.punctuation
    special_chars_list = list(special_chars_string)
    for i in special_chars_list: #remove punctuation and spaces from the word
        sent = sent.replace(i, "")

    sent = sent.lower()#normalize to lowercase
    sent_list = sent.split()#split into words and ignore empty tokens

    longest_word = ""
    longest_length = 0
    for word in sent_list:#loop through the list
        if len(word) > longest_length:#check the lenght of each word and compare it to the longest word length
            longest_word = word#if the word is longer than the longest word, update the longest word and its length
            longest_length = len(word)

    print(f"The longest word is '{longest_word}' with {longest_length} characters.")#output the longest word and its length

#test phrase: "Coding is both fun and challenging", "Hello, world! Hello!!!", "Hello guys", "This is a unique sentence.", "th!is this",
longest_word()
