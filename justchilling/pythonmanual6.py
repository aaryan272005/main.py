'''Simple calculator using functions'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", add(a,b))
elif choice == 2:
    print("Result:", subtract(a,b))
elif choice == 3:
    print("Result:", multiply(a,b))
elif choice == 4:
    if b != 0:
        print("Result:", divide(a,b))
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice.")

