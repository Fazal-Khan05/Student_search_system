def calculate_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def assign_grade(average):  
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

with open('grades.txt', 'a') as file:
    for i in range(num_students):
        student_name = input(f"Enter the name of student {i + 1}: ")
        roll_no = input(f"Enter roll number for {student_name}: ")
        marks = []

        for j in range(num_subjects):
            mark = float(input(f"Enter marks for subject {j + 1} for {student_name}: "))
            marks.append(mark)
        
        total, average = calculate_avg(marks)
        grade = assign_grade(average)

        print(f"The average marks for {student_name} are: {average:.2f}")
        print(f"Grade for {student_name}: {grade}")

with open('grades.txt', 'a') as file:
        file.write(f"Name: {student_name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Total Marks: {total}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {grade}\n")
        file.write("-" * 28 + "\n")
