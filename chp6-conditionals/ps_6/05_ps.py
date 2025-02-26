'''Write a program to find weather your name is in the list or not'''

# List of names

names = ["Aaryan","Om","Abhinav","NiggaXshardul","Harsh","keshav","Steffi"]

# Ask the user for their name

user_name = input("Enter your name: ")

# Check if the user's name is in the list

if user_name in names:

    print(f"{user_name} is in the list.")

else:
    print(f"{user_name} is not in the list")

'''
Output:
Enter your name: Sherkhane
Sherkhane is not in the list
'''