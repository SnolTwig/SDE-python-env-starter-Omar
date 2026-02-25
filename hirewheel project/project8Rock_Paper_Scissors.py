"""
1. import random libary
2. initialize roshambo = [ ROCK, PAPER, or SCISSORS], and win = false
3. randomly select from that list to make computer_choice
4. prompt the user to pick from roshambo list set that equal to user_choice
5a. if the user doesn't pick from the list ask them again
5. the set user_choice to upercase
6. compare user_choice and computer_choice and see who wins
7. if the user wins set win = true and print you win
8 if the user loses, print you lost
"""
import random
def rock_paper_scissors():
    roshambo = ["ROCK", "PAPER", "SCISSORS"]#initialize roshambo = [ ROCK, PAPER, or SCISSORS], and win = false
    win = False
    computer_choice = random.choice(roshambo)#Generates a random choice for the computer from the roshambo list
    user_choice = input("Please choose ROCK, PAPER, or SCISSORS: ").upper().strip()#prompt the user to pick from roshambo list set that equal to user_choice and normalize to uppercase and remove spaces

    while user_choice not in roshambo:#if the user doesn't pick from the list ask them again
        print("Invalid choice. Please try again.")
        user_choice = input("Please choose ROCK, PAPER, or SCISSORS: ").upper()

    if user_choice == computer_choice:#compare user_choice and computer_choice and see who wins
        print("It's a tie!")
        return
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or (user_choice == "PAPER" and computer_choice == "ROCK") or (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        win = True
    else:
        win = False

    if win:#if the user wins set win = true and print you win
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {user_choice}, and the computer chose {computer_choice}. You lost!")
rock_paper_scissors()
