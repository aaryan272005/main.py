'''Write a program to find out weather the post is about a specific thing'''

# Taking input from the user about what the want to check in the post/blog/essay/article 
particular = input("Enter the specific thing to verfiy : ")
post = input("Enter the post you want to search in :")
if particular in post.lower():
    print(f"The post is about the {particular} ")
else:
    print(f"The post does not contain the {particular} ")