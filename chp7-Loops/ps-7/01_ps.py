'''Write a program to print multiplication table of a given number using for loop'''

# Input the number from the user
num = int(input("Enter the number: "))

# Print the multiplication table
for i in range(1,11):
    print(f"{num}x{i}={num*i}")
