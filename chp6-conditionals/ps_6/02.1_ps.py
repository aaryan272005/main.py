'''A program that calculates marks & total percentage of 1 or n subject (user defined) '''

# NOTE:In this program, we are using dictionary to store the marks of each subject. This makes it easy to retrieve the marks for a particular subject.
# Also, we are using if-else statements to determine whether a student passed or failed in an individual subject.
# Finally, we are calculating the total marks and total percentage using the provided formula.
# The program also includes comments for better understanding.

# Ask user number of subjects
no_subjects = int(input("Enter the number of subjects: "))

# Initializeing empty dictionary of subjects
subjects = {}

# Loop to get subject names and marks
for i in range(no_subjects):
    subject_name = input(f"Enter subject name {i+1}: ")
    subject_marks = float(input(f"Enter marks in {subject_name}: "))
    subjects[subject_name] = subject_marks
    # using if-else to determine whether passed in an individual subject
    if subject_marks>=35 :
        print(f"{subject_name} passed.")
    else: 
        print(f"{subject_name} failed.")
     
# Calculate total marks
total_marks = sum(subjects.values())

# Calculate total percentage
total_percentage = (total_marks / (no_subjects * 100)) * 100


# Print results
print("Total marks scored :", total_marks)
print("Total percentage :", total_percentage)
if total_percentage >= 40:
    print("Student passed in all subjects!!!")
else :
    print("Student has failed!!")


'''
Output :
case 1:
        Enter the number of subjects: 3
        Enter subject name 1: math
        Enter marks in math: 99
        math passed.
        Enter subject name 2: chem
        Enter marks in chem: 40
        chem passed.
        Enter subject name 3: physics
        Enter marks in physics: 22
        physics failed.
        Student passed in all subjects!!!
        Total marks scored : 161.0
        Total percentage : 53.666666666666664

case 2:
        Enter subject name 2: chemistry
        Enter marks in chemistry: 11
        chemistry failed.
        Total marks scored : 33.0
        Total percentage : 16.5
        Student has failed!!
'''


