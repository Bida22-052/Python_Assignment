def get_grade_input(subject):
    """Get a valid grade for a given subject."""
    while True:
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_subject_grades():
    """Get grades for all subjects."""
    subjects = ['Math', 'English', 'Science']
    grades = {}
    for subject in subjects:
        grades[subject] = get_grade_input(subject)
    return grades

def add_student(students):
    """Add a new student and their grades."""
    name = input("Enter the student's name: ")
    if name in students:
        print(f"{name} already exists.")
    else:
        students[name] = get_subject_grades()

def update_student_grades(students):
    """Update grades for an existing student."""
    name = input("Enter the student's name to update: ")
    if name in students:
        students[name] = get_subject_grades()
    else:
        print(f"Student {name} does not exist.")

def remove_student(students):
    """Remove a student from the system."""
    name = input("Enter the student's name to remove: ")
    if name in students:
        del students[name]
        print(f"Student {name} has been removed.")
    else:
        print(f"Student {name} does not exist.")

def calculate_averages_and_extremes(students):
    """Calculate average grades and show highest and lowest per subject."""
    subject_names = ['Math', 'English', 'Science']
    subject_grades = {subject: [] for subject in subject_names}

    for name, grades in students.items():
        average_grade = sum(grades.values()) / len(grades)
        print(f"{name}'s average grade: {average_grade:.2f}")

        for subject in subject_names:
            subject_grades[subject].append(grades[subject])

    for subject in subject_names:
        highest = max(subject_grades[subject])
        lowest = min(subject_grades[subject])
        print(f"{subject} - Highest grade: {highest}, Lowest grade: {lowest}")

def search_student(students):
    """Search for a student by name and display their grades."""
    name = input("Enter the student's name to search: ")
    if name in students:
        grades = students[name]
        average = sum(grades.values()) / len(grades)
        print(f"Name: {name}, Grades: {grades}, Average: {average:.2f}")
    else:
        print(f"Student {name} not found.")

def display_student_summary(students):
    """Display a summary of all students and their grades."""
    for name, grades in students.items():
        average_grade = sum(grades.values()) / len(grades)
        grades_str = ', '.join(f"{sub}: {grade}" for sub, grade in grades.items())
        print(f"Name: {name}")
        print(f"Grades: {grades_str}")
        print(f"Average Grade: {average_grade:.2f}")
        print()

def main():
    students = {}
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Update Student Grades")
        print("3. Remove Student")
        print("4. Calculate Averages and Extremes")
        print("5. Search Student")
        print("6. Display Student Summary")
        print("7. Exit")

        option = input("Select an option: ")
        if option == '1':
            add_student(students)
        elif option == '2':
            update_student_grades(students)
        elif option == '3':
            remove_student(students)
        elif option == '4':
            calculate_averages_and_extremes(students)
        elif option == '5':
            search_student(students)
        elif option == '6':
            display_student_summary(students)
        elif option == '7':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
