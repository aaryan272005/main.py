'''Write a program to create a dictionary of hindi words with the values as their English words 
translation , provide user with an option to look it up!'''

# dictionary of hindi words with their english translations
d={"hindi":"english",
   "tu":"you",
   "mai":"me",
   "madat":"help"}

# user input for lookup
word = input("Enter the word you want the meaning of: ")

# checking if word is in dictionary

if word in d:
    print(f"The meaning of {word} is {d[word]}")
else:
    print("The word is not in the dictionary!")