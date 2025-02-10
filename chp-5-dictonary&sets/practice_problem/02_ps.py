'''Write a program to take the input of total 8 numbers and display all the unique numbers(once) '''
# Input: number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty set to store unique numbers
s = set()

# Take 'n' inputs from the user
print(f"Enter {n} numbers:")
for i in range(n):
    num = int(input())  # Convert input to integer
    s.add(num)  # Add to set (ensures uniqueness)

# Display unique numbers
print("Unique numbers are:")
for num in s:
    print(num)