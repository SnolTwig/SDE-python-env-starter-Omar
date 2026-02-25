import random
def player_guess(num):
    secret_number = num
    print("welcome to Bulls and Cows game! In this game, you have to guess a 4-digit number. For each guess, you will receive feedback in the form of 'Bulls' and 'Cows'. A 'Bull' indicates a correct digit in the correct position, while a 'Cow' indicates a correct digit in the wrong position. You have 15 tries to guess the number. Good luck!")

    for i in range(15):#15 tries
        guess = input("Enter your 4-digit guess: ")#get user input

        while not guess.isdigit():#check if input is a number
            print("Invalid input. Please enter a 4-digit number.")
            guess = input("Enter your 4-digit guess: ")

        while len(guess) != 4 and not guess.isdigit():#check if input is 4 digits
            print("Your guess must be 4 digits long.")
            guess = input("Enter your 4-digit guess: ")

        bulls = 0
        cows = 0
        for j in range(4):#check for bulls and cows
            if guess[j] == secret_number[j]:
                bulls += 1
            elif guess[j] in secret_number:
                cows += 1
        print(f"{bulls} Bulls, {cows} Cows")
        if bulls == 4:
            print("Congratulations! You've guessed the number!")
            return
    print(f"Sorry, you've used all your tries. The number was {secret_number}.")


secret_number = ''.join(random.sample("0123456789", 4)) #gnerate a random 4-digit number with unique digits, creadit @Copperfield from stackoverflow
player_guess(secret_number)
