'''Write a program to calculate the grade of a student from his marks form the following scheme
90-100 => Ex
80-90 => A
70-80 => B
60-70 => C
50-60 => D
<50 => F'''

marks = int(input("Enter your marks: "))

if marks<=100 and marks>=90 :
    grade = "Ex"
    print(f"Your grade is {grade}")

elif marks<90 and marks>=80:
    grade = "A"
    print(f"Your grade is {grade}")

elif marks<80 and marks>=70:
    grade = "B"
    print(f"Your grade is {grade}")

elif marks<70 and marks>= 60:
    grade = "C"
    print(f"Your grade is {grade}")

elif marks<60  and marks>= 50:
    grade = "D"
    print(f"Your grade is {grade}")

elif marks<50:
    grade = "F"
    print(f"Your grade is {grade}")

'''
Output:
Enter your marks: 90
Your grade is Ex
'''