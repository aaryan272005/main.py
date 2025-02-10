# *To access characters in a string*

a = "Aaryan Sherkhane"
name = "Aaryan"
nameshort = name[0:3]  # Start form incdex 0 all the way till 3 (exceluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# *String Slicing*

# NOTE: This is normal number line
# NOTE: first index is included and last in not included
# positive always starts form 0
print(a[0:7])
# NOTE:negative always starts form -1
print(a[-10:-1])
print(a[:7])  # By default 0
print(a[0:])  # By default -1

# *String Concatenation*

b = "abcdefghijklmnopqrstuvwxyz"

print(b[1:9:4])  # First mltb jaha se counting start karna hai
# Secong mltb jaha tak karna hai (last wala excude hoga)
# Third mltb utne alpabelts jump karna hai (First alpahabet will always be inculded)
