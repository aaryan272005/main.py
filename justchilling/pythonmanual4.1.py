  
def records():
    no_of_students = int(input("Enter the number of students: "))
    students = []  # List to store student dictionaries

    for i in range(no_of_students):
        student = {}  # Create a new dictionary for each student
        student["Name"] = input(f"Enter the Name of student {i+1}: ")
        student["Grade"] = input(f"Enter the Grade of student {i+1}: ")
        student["Attendance"] = input(f"Enter the Attendance of student {i+1}: ")
        students.append(student)  # Store each student's data in the list

    print("\nStudent Records:")
    for student in students:
        print(student)  # Display all student dictionaries at once

records()