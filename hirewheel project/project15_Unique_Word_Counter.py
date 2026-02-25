"""
Problem 3 · Unique Word Counter
Count total and unique words in a sentence.

python_basics
Tackle the problem in your preferred IDE first. When you are confident in your code, document your UCASE notes, paste your solution, and record how you validated it. Auto-evaluation will help us track how your skills evolve.
Challenge Overview
Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.
Examples

Input: "Code code build!"
Output: "Total words: 3, Unique words: 2"
The word "code" appears twice.
"""
'''
1. get user input
2. normalize to lowercase and remove punctuation
3. convert to list of words
4. count total words and unique words
5. output total words and unique word count
'''
import string
def count_unique_words():
    sent = input("Enter a sentence: ")#get user input

    while sent == "" or sent.isspace(): #if the user enters nothing or only whitespace
        print("You must enter a sentence")#prompt the user again
        sent = input("Enter a sentence: ")

    special_chars_string = string.punctuation#get a string of punctuation characters
    special_chars_list = list(special_chars_string)#convert the string to a list
    for i in special_chars_list:#remove punctuation from the sentence
        sent = sent.replace(i, "")

    sent = sent.lower()#normalize to lowercase
    snet_list = sent.split()#split into words and ignore empty tokens

    total_words = len(snet_list)#count total words
    unique_words = len(set(snet_list))#count unique words by converting the list to a set and getting its length
    print(f"Total words: {total_words}, Unique words: {unique_words}")
count_unique_words()

#test phrase: "Code code build!", "Hello, world! Hello!!!", "Hello guys", "This is a unique sentence.", "th!is this",
#changes: 
