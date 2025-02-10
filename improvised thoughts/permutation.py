#permutation
import math
n=int(input("Enter total number of items :")) #total number of items
r=int(input("Enter Number of items you want to arrange:")) #number of items to be arranged 
m=math.perm(n,r)
print(f"Number of ways to arrange {r} items out of {n} are {m}")