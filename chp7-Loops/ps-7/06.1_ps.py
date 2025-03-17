'''Write a program to calculate the factorial of a given number using for loop.'''
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"The factorial of {num} is {fact}")
# Output:
# Enter a number: 5
# The factorial of 5 is 120
# Enter a number: 10
# The factorial of 10 is 3628800

import math
num = int(input("Enter a number: "))
fact = math.factorial(num)
print(f"The factorial of {num} is {fact}")
