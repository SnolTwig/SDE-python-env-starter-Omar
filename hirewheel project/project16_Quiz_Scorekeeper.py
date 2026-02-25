"""Challenge Overview
Score a multiple-choice quiz from an answer key and user answers.

Prompt for the answer key as a comma-separated list (A/B/C/D).
Prompt for the user's answers in the same format.
Compare answers position-by-position and count correct responses.
Output the score as a count and percent; handle mismatched lengths gracefully.
Examples

Input: key=A,B,C,D user=A,B,D,D
Output: "Score: 75% (3/4 correct)"
Only the third answer differs.
    """

def answer_key():# Function to get and validate the answer key from user input
    key_input = ""
    while key_input.strip() == "" :  # Ensure user input is not empty
        key_input = input("Enter the answer key (comma-separated A/B/C/D): ")
        key = key_input.strip().upper()#Convert to lists and clean whitespace
        key_list = key.split(",")

        for i in range(len(key_list)):# Clean whitespace between grades from key answers
            key_list[i] = key_list[i].strip()

        for answer in key_list:
            if answer not in acceptable_answers:
                print(f"Invalid answer '{answer}' in key. Please enter only A/B/C/D.")
                key_input = ""  # Reset to prompt again
    return key_list

def user_answers():# Function to get and validate the user's answers from user input
    user_input = ""
    while user_input.strip() == "":  # Ensure user input is not empty
        user_input = input("Enter the user's answers (comma-separated A/B/C/D): ")
        user = user_input.strip().upper()#Convert to lists and clean whitespace
        user_list = user.split(",")
        for i in range(len(user_list)):# Clean whitespace between grades from user answers
            user_list[i] = user_list[i].strip()

        for answer in user_list:
            if answer not in acceptable_answers:
                print(f"Invalid answer '{answer}' in user's answers. Please enter only A/B/C/D.")
                user_input = ""  # Reset to prompt again
    return user_list

#Prompt for inputs
acceptable_answers = {"A", "B", "C", "D"}  # Set of acceptable characters

key_list = answer_key()  # Get the answer key from user input
user_list = user_answers()  # Get the user's answers from user input

# Compare position-by-position
correct = 0
min_length = min(len(key_list), len(user_list))
for i in range(min_length):
    if key_list[i] == user_list[i]:
        correct += 1

total = len(key_list)# Total questions is based on the answer key length
if total > 0:# Avoid division by zero
    percent = round((correct / total) * 100)
else:
    percent = 0

# Output result
print(f"Score: {percent}% ({correct}/{total} correct)")
