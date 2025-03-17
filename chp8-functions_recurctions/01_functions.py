#function is a group of statements that performs a specific task
#When a program gets bigger in size and its complexity grows,it gets difficult for a programmer to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of times

def avg():#defining a function
    '''This function calculates the average of three numbers'''
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    average = (num1 + num2 + num3) / 3
    print(f"The average of {num1}, {num2} and {num3} is {average}")
    
avg()#calling the function avg() to execute 
