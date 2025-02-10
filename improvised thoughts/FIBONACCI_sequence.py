# finonacci sequences
# 0 1 1 2 3 5 8 13 21 34 

n=int(input("Enter the range:")) 

a=0
b=1

print(f" {a}  {b}",end=" ")

for i  in range (n-2):
    c=a+b
    print(f" {c}",end=" ")
    a=b
    b=c