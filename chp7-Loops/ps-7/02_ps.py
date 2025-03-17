'''
Write a program to greet all the persons names stored in a list 'l' and which start with S.
l=["Harry","Sohan","Sachin","Rahul"]
'''
l=["Harry","Sohan","Sachin","Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello "+name)