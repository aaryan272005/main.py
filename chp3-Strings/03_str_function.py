"""String Functions"""

#NOTE: String remains the same,using a function means creating a whole new String


# Some of the mostly used  functions to perform opertions on or manipulate strings are:

# 1. '''len(): returns the length of the string

# 2. Stringwithend("an") -> This functions tells weather the variable string ends when the string end with
# the string "an" or not. if string is " Aaryan", it returns true for "an" since Aaryan end with an

# 3. string.count("c") -> count the total number of occurrences of any chatacters

# 4. string.capitalize() -> This function capitalize the first character of a given string

# 5. string.find(word) -> This function find a word and returns the index of first occurence of that word in the string

# 6. string.replace(oldword,newword) -> This function replace the oldword with newword in the enter string

name = "aaryan"

print(len(name))
print(name.startswith("aa"))  # Capital letters are different
print(name.endswith("an"))  # It is case sensitive
print(name.capitalize())  # have effect only on the first character
print(name.replace("  "," ")) # replace


