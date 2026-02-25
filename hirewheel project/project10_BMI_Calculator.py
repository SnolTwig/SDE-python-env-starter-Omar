
def get_weight():#get user weight input
    weight = input("Please enter your weight in kilograms: ")
    try:#convert weight to float
        weight = float(weight)
        return weight
    except ValueError:#handle invalid input
        print("Invalid input. Please enter a numeric value for weight.")
        return get_weight()

def get_height():#get user height input
    height = input("Please enter your height in meters: ")
    try:#convert height to float
        height = float(height)
        return height
    except ValueError:#handle invalid input
        print("Invalid input. Please enter a numeric value for height.")
        return get_height()

height = get_height()#get user height input
weight = get_weight()#get user weight input
#calculate BMI
bmi = weight / (height ** 2)
bmi = round(bmi, 2)
#determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"
#print result
print(f"Your BMI is {bmi}, which is considered {category}.")
