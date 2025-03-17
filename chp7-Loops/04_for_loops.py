# A for loop is used to iterate through a sequence like list,tuple or string[iterables]
# Syntax:
list=[1,3,4]
for items in list:
    print(items) # Output: 1 3 4

#Range function in python 
# The range() function is used to generate a sequence of numbers.
# We can also specify the start,stop and step size as follows
# range(start,stop,step_size)

# An Example: to demonstrate range() function
for i in range(0,7):#range(7) can also be used.
    print(i) # prints 0 to 6

'''For loop with else'''
# An optional else can be used with a for loop if the code is to be executed when the loops exhausts.

# example:
list=[1,2,3,4,5]
for i in list:
    print(i)
else:
    print("No more elements in the list")#This is printed when the loop eshausts

'''
output:
1
2
3
4
5
No more elements in the list
'''
