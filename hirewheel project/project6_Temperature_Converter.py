
def cel_to_fah(c):#Celsius to Fahrenheit
    return (c * 9/5) + 32

def cel_to_kel(c):#Celsius to Kelvin
    return c + 273.15

def fah_to_cel(f):#Fahrenheit to Celsius
    return (f - 32) * 5/9

def fah_to_kel(f):#Fahrenheit to Kelvin
    return (f - 32) * 5/9 + 273.15

def kel_to_cel(k):#Kelvin to Celsius
    return k - 273.15

def kel_to_fah(k):#Kelvin to Fahrenheit
    return (k - 273.15) * 9/5 + 32

def validate_temperature(scale):#validate temperature input
    from_scale = scale
    try:#get temperature value
        value = float(input(f"Enter the temperature value in {from_scale}: "))
    except ValueError:
        print("Please enter a valid numeric temperature.")
        validate_temperature(scale)
        return value
    return value

def temperature_converter():#
    print("Welcome to the Temperature Converter!")
    from_scale = ""
    to_scale = ""

    while from_scale not in ['C', 'F', 'K']:#validate input
        from_scale = input("Enter the scale you are converting from (C/F/K): ")
        from_scale = from_scale.strip()
        from_scale = from_scale.upper()

    while to_scale not in ['C', 'F', 'K']:#validate input
        to_scale = input("Enter the scale you are converting to (C/F/K): ")
        to_scale = to_scale.strip()
        to_scale = to_scale.upper()

    while from_scale == to_scale:#check if scales are the same
        print("The 'from' and 'to' scales cannot be the same. try again.")

        while from_scale not in ['C', 'F', 'K']:#validate input
            from_scale = input("Enter the scale you are converting from (C/F/K): ")
            from_scale = from_scale.strip()
            from_scale = from_scale.upper()
            
        while to_scale not in ['C', 'F', 'K']:#validate input
            to_scale = input("Enter the scale you are converting to (C/F/K): ")
            to_scale = to_scale.strip()
            to_scale = to_scale.upper()

    value = validate_temperature(from_scale)

    if from_scale == 'C':#Celsius conversions
        if to_scale == 'F':#Celsius to Fahrenheit
            converted_value = cel_to_fah(value)
            print(f"{value}° Celsius is {converted_value}° Fahrenheit.")
        elif to_scale == 'K':#Celsius to Kelvin
            converted_value = cel_to_kel(value)
            print(f"{value}° Celsius is {converted_value} Kelvin.")
    elif from_scale == 'F':#Fahrenheit conversions
        if to_scale == 'C':#Fahrenheit to Celsius
            converted_value = fah_to_cel(value)
            print(f"{value}° Fahrenheit is {converted_value}° Celsius.")
        elif to_scale == 'K':#Fahrenheit to Kelvin
            converted_value = fah_to_kel(value)
            print(f"{value}° Fahrenheit is {converted_value} Kelvin.")
    elif from_scale == 'K':#Kelvin conversions
        if to_scale == 'C':#Kelvin to Celsius
            converted_value = kel_to_cel(value)
            print(f"{value} Kelvin is {converted_value}° Celsius.")
        elif to_scale == 'F':#Kelvin to Fahrenheit
            converted_value = kel_to_fah(value)
            print(f"{value} Kelvin is {converted_value}° Fahrenheit.")
    else:
        print("Invalid temperature scale entered.")
temperature_converter()
