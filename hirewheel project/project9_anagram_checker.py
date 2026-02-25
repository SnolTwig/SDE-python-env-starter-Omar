def anagram_checker(): #makes the word ready for anagram checking
    word = input("Enter a word: ") #get user word
    if word == "": #if the user enters nothing
        print("You must enter a word")
        anagram_checker()
    try:# handling non string inputs
        word = word.lower()
        punc = (" ", ".", ",", "?", "/","'",'"', "\\", "!", ";", ":")#removing punctuation and spaces
        for i in punc:
            word = word.replace(i, "")
        if word == []:#if the nomalized word is empty
            print("You must new enter a word")
            anagram_checker()
        word = list(word) # converting the string to a list
        word = sorted(word)# makes the list aplhabetically ordered
        return word
    except AttributeError:
        print("Your word is not a string, please try again")
        anagram_checker()

word1 = anagram_checker()
word2 = anagram_checker()

if word1 == word2: #comparing the two words
   print("This is an anagram")
else:
   print("This is not an anagram")
