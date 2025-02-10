'''Write a program to fill the letter template given below with name and date'''


letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Aaryan").replace("<|Date|>","27 December 2005"))
#NOTE: Another way to do this is :

name = input("Enter the name:")
date = input("Enter the date:")

print (f"letter =\nDear {name},\nYou are selected!\n{date}")