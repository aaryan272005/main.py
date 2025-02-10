#Write a program to find out weather a student has passed or failed if it requires a total of 40%
# and altest 33% in each subject to pass Assume their are 3 subjects and take marks as an
# input from the user
list = ["Physics","Chemistry","Maths"]
total_marks = 100

for subject in list:
    marks = int(input(f"Enter marks in {subject}: "))
    if marks >= 0.33 * total_marks:
        print(f"{subject} has passed.")
    else:
        print(f"{subject} has failed.")

if (0.40 * total_marks) <= (sum(int(f"Enter marks in {subject}: ")) for subject in list):
    print("Student has passed in all subjects!!!")
else:
    print("Student has Failed!!")

