'''Factorial using math module'''
import math
n=int(input("Enter a number: "))
factorial = math.factorial(n)
print(f"The factorial of {n} is {factorial}")

'''Factorial using while loop'''
f=1
i=1
n=int(input("Enter a number: "))
while i<=n:
    f=f*i
    i=i+1
    print(f)

'''Factorial using for loop'''
f=1
n=int(input("Enter a number: "))

for i in range(1,n+1):
    f=f*i
    print(f)

