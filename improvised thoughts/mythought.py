'''Using for loop to make a program to add fruits in the list'''

# Initialize an empty list to store the fruits
fruits = []

# Ask the user how many fruits they want to enter
num_fruits = int(input("How many fruits would you like to enter? "))

# Use a for loop to get the fruit names from the user
for i in range(num_fruits):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

# Display the list of fruits entered by the user
print(f"The list of fruits you entered is:\t{fruits}")
