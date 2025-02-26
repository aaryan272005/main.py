#Create a empty dictionary allow 'n' friends to enter their favourite language as value 
#and use key as their name and assume as their name as unique

# Creating an empty dictionary
d={}

# Enter how many friends to enter their favourite language
num_friends=int(input("Enter the number of friends: "))

# Use a for loop to get the friends names and their favourite language from the user
for i in range(num_friends):
    name=(input(f"Enter the name {i+1}:"))
    lang=(input("Enter the favourite language:"))

    #adding/updating the name and lang in dictionary
    d.update({name:lang})
    #displaying the name and lang in dictionary
    print(d)
