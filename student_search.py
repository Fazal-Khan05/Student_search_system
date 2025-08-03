def search_student(file_path, keyword):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        found = False
        student_block = []

        for line in lines:
            if line.strip() == "-" * 28:
                block_text = ''.join(student_block)
                if keyword.lower() in block_text.lower():  # ✅ Fixed here
                    print("Student found:\n")
                    print(block_text)
                    print("-" * 28)
                    found = True
                student_block = []  # Clear for next student
            else:
                student_block.append(line)

        if not found:  # ✅ Moved outside the loop
            print("No student found with the given keyword.")

# Get input and call function
search = input("Enter the name or roll number of the student to search: ")
file_path = 'grades.txt'
search_student(file_path, search)
