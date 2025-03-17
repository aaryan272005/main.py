'''Write a program to print the following star pattern:
***
* *
***
for n = 3
'''
n = int(input("Enter the number of rows: "))

# Print the first row
print("*" * n)

# Print the remaining rows
for i in range(2, n):
    print("*" + " " * (n - 2) + "*")

# Print the last row
print("*" * n)
