def tip_splitter():
    while True:#keep asking for the tip percentage until a valid integer is entered
        try:#try to convert the input to an integer, if it fails, catch the ValueError and prompt the user again
            tip_percent = int(input("Please enter the tip percentage you would like to give (e.g., 15 for 15%): "))
        except ValueError:
            print("Invalid input for tip percentage. Please enter a whole number.")
            continue
        if tip_percent < 0:#check if the tip percentage is negative, if it is, prompt the user again
            print("Tip percentage cannot be negative. Please enter a non-negative whole number.")
            continue
        break

    while True:#keep asking for the bill amount until a valid float is entered
        try:#try to convert the input to a float, if it fails, catch the ValueError and prompt the user again
            bill = float(input("Please enter the total bill amount: "))
        except ValueError:
            print("Invalid input for bill amount. Please enter a numeric value.")
            continue
        if bill < 0:#check if the bill amount is negative, if it is, prompt the user again
            print("Bill amount cannot be negative. Please enter a non-negative numeric value.")
            continue
        break

    while True:#keep asking for the number of people until a valid integer greater than 0 is entered
        num_ppl = input("Please enter the number of people to split the bill: ")
        if num_ppl.isdigit() and int(num_ppl) > 0:#check if the input is a digit and greater than 0
            num_ppl = int(num_ppl)
            break
        else:
            print("Invalid input for number of people. Please enter a whole number greater than 0.")

    tip_dollar = round(bill * (tip_percent / 100), 2)#calculate the tip amount in dollars by multiplying the bill by the tip percentage divided by 100, and round it to 2 decimal places
    total = bill + tip_dollar#calculate the total bill by adding the original bill and the tip amount
    per_person = round(total / num_ppl, 2)#calculate how much each person should pay by dividing the total bill by the number of people, and round it to 2 decimal places

    print(f"Total bill (including tip): ${total},Tip amount: ${tip_dollar}, Each person should pay: ${per_person}")

tip_splitter()
