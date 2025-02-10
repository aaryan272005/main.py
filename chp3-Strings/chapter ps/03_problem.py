'''Write a program to detect double space in the string'''
name = "Aaryan   is a programer!!!"
    #          ^
    #          |
    #          Double space found
    #          Start index 
print(name.find("  "))