'''
Break statement:
'break' is used to come out of the loop when encountered. It instructs the program to exit the loop now

Continue statement:
'continue' is used to stop the current iteration of the loop and continue with the next iteration of the loop.
It instructs the program to skip the current iteration and continue with the next iteration of the loop.

Pass Statement:
pass is a null statement in python. It instructs to "do nothing".
'''

for i in range (100):
    if i==10:
        break# Exits the loop when i=10
    print(i)

for i in range (100):
    if i==10:
        continue # Skips the current iteration when i=10
    print(i)

for i in range (100):
    pass # Without pass,the program will throw an error 