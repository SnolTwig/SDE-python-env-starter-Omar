def is_prime():
    try:
        num = int(input("Please enter a positive integer: "))#user input a number

        while num < 0:#check for positive integer
            print("That is not a positive integer. Please try again.")
            num = int(input("Please enter a positive integer: "))

        if num == 0 or num == 1:#check for 0 and 1
            print(num, "is not a prime number.")
            return
        primes_list = [2]#list to hold prime numbers

        for i in range(3, num+1):#cycles through all numbers between 3 and the user input number
            z = False
            for j in range(2, i):#cycles through all numbers between 2 and the current number to check for factors
                y = i % j#check for factors
                if y == 0:#if a factor is found, the number is not prime
                    z = True
                    break
            if z:#if number is not prime, prevent it from being added to the primes list
                continue
            primes_list.append(i)#add prime number to the list

        if num == primes_list[len(primes_list)-1]:#check if the user input number is in the primes list
            primes_list = ", ".join(str(x) for x in primes_list) #credit Mateen Ulhaq from stack overflow for this line, converts list to string
            print(num, "is a prime number.")
            print("Primes up to", num, "are:", primes_list)
        else:
            primes_list = ", ".join(str(x) for x in primes_list) #credit Mateen Ulhaq from stack overflow for this line, converts list to string
            print(num, "is not a prime number.")
            print("Primes up to", num, "are:", primes_list)
    except ValueError:
        print("That is not a valid input. Please try again.")#handle ValueError
        is_prime()

is_prime()
