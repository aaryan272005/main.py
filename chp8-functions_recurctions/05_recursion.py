'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
factorial(5) = 120
factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n=int(input("Enter a number: "))
print (factorial(n))