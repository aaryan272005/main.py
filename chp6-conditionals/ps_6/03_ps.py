'''A spam comment is defined as a text containing following keywords:
"make a lot of money", "buy now", "subscribe this", "click this"
Write a program to detect this spams.'''

comment = input("Enter a comment:")

sentence1 = "make a lot of money"
sentence2 = "buy now"
sentence3 = "subscribe this"
sentence4 = "click this"

if((sentence1 in comment) or (sentence2 in comment) or (sentence3 in comment) or (sentence4 in comment)):
	print("This is a spam comment.")
else:
	print("This is normal comment.")

''' 
Output:
Enter a comment: chick this and make a lot of money
This is a spam comment.
'''