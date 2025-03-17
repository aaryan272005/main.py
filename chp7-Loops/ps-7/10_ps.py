'''Write a program to print multiplication of n using for loop in reverse order.'''
num = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")
# Output:
# Enter a number: 5
# 5 x 10 = 50
