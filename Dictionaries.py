# Function to manage subject grades for each student
def get_subject_grades():
    subjects = ['Math', 'English', 'Science']
    grades = {}
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return grades


# Add, update, remove students in the dictionary
def manage_students(students):
    while True:
        print("\n1. Add Student\n2. Update Grades\n3. Remove Student\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in students:
                print(f"{name} already exists.")
            else:
                grades = get_subject_grades()
                students[name] = grades

        elif choice == '2':
            name = input("Enter student name to update grades: ")
            if name in students:
                grades = get_subject_grades()
                students[name] = grades
                print(f"{name}'s grades have been updated.")
            else:
                print(f"Student {name} not found.")

        elif choice == '3':
            name = input("Enter student name to remove: ")
            if name in students:
                del students[name]
                print(f"{name} has been removed.")
            else:
                print(f"Student {name} not found.")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")


# View grades for a specific subject across all students
def view_subject_grades(students, subject):
    print(f"\nGrades for {subject}:")
    for name, grades in students.items():
        if subject in grades:
            print(f"{name}: {grades[subject]}")
        else:
            print(f"{name} has no grade for {subject}")


# Search for a specific student and calculate their average
def search_student(students):
    name = input("Enter the student's name to search: ")
    if name in students:
        grades = students[name]
        average_grade = sum(grades.values()) / len(grades)
        print(f"{name}'s grades: {grades}")
        print(f"Average grade: {average_grade:.2f}")
    else:
        print(f"Student {name} not found.")


# Main function to run the system
def main():
    students = {}
    while True:
        print("\n1. Manage Students\n2. View Subject Grades\n3. Search for Student\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_students(students)
        elif choice == '2':
            subject = input("Enter subject name: ")
            view_subject_grades(students, subject)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
