# Write a program to check whether a given username contains less than 10 characters or not.

username = input("Enter a username: ")
if (len(username) >= 10):
    print(f"The entered username '{username}' is not less than 10 characters.")
else:
  print(f"The entered username '{username}' is less than 10 characters.")

'''
Output:
Case1: 
      Enter a username: AaryanSherkhane
      The entered username 'AaryanSherkhane' is not less than 10 characters.

Case2: 
      Enter a username: Aaryan
      The entered username 'Aaryan' is less than 10 characters. 
'''