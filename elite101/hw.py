vowel = ["a","e","i","o","u","A","E","I","O","U"]

def count_vowels(word):
    count = 0
    for i in word:
        for j in vowel:
            breakpoint()
            if i == j:
                count += 1
    return count
word = input("Enter String: ")
print(count_vowels(word))
breakpoint()
