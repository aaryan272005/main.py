'''factorial of a number using while loop'''
n=int(input("Enter a number :"))
i=1
f=1
a=1
while i<=n:
    f=f*i
    i=i+1
    print(f)

'''Factorial of a number using for loop'''
for i in range(1,n+1):
    a=a*i
    print(a)

'''Factorial of a number using math module'''
import math 
n=int(input("Enter a number: "))
math.factorial(n)
print(f"The factorial of {n} is {math.factorial(n)}")


