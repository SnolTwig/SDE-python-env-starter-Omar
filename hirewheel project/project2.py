'''
Done
'''
import random

#takes users input
def user_input():
    user_num = input("please enter a random number between 1-100:")
    #converts user input into a intager value
    try:
        user_num = int(user_num)
    #handles ValueError and reruns the function
    except ValueError:
        print("That's not a vaild input, try again:")
        user_input()
    return user_num

#generates the secret number
secret_num = random.randint(1,100)
guess = user_input()

#compares guess to the secret number.
while secret_num != guess:
    if guess > secret_num:
        print("you guesed to high, try again")
        guess = user_input()
    if guess < secret_num:
        print("you guesed to low, try again")
        guess = user_input()
print("you guesed correct, thanks for playing")
