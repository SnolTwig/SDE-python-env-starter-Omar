"""
1.fibonacci = [0,1]
2. n = -1
3. while is not a digit or less than 0
   n = input(" how many Fibonacci number do you want?")
4. if n= 0
    print("0")
5. elif n=1
    fib_string = ", ".join(fibonacci)
6. else
    while fibonacci < n
        new_ value = fibonacci(-1) + fibonacci(-2)
        fibonacci.append(new_value)
    fib_string = ", ".join(fibonacci)

Generate and display the Fibonacci sequence up to N terms.

Prompt the user for the number of terms N (must be a positive integer).
Generate the Fibonacci sequence starting from 0 and 1.
Handle edge cases: N=1 returns just [0], N=2 returns [0, 1].
Display the full sequence as a comma-separated list.
Examples

Input: N=8
Output: "0, 1, 1, 2, 3, 5, 8, 13"
Each number is the sum of the two preceding numbers.
"""

fibonacci = [0, 1]
n = -1
while not str(n).isdigit() or int(n) < 0:
    n = input("How many Fibonacci numbers do you want? ")
n = int(n)
if n == 0:
    print("0")
elif n == 1:
    fib_string = ", ".join(fibonacci)
else:
    while len(fibonacci) < n:
        new_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(new_value)
    fib_string = ", ".join(fibonacci)
