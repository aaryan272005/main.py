'''Write a program to find the sum of the n natural numbers using while loop.'''
num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum += i
    i += 1
print(f"The sum of the first {num} natural numbers is {sum}")
# Output:
# Enter a number: 5
# The sum of the first 5 natural numbers is 15
# Enter a number: 10
# The sum of the first 10 natural numbers is 55
