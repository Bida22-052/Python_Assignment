def get_subject_grades():
    subjects = ['Math', 'English', 'Science']
    grades = []
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return grades


def calculate_averages_and_extremes(students):
    subject_names = ['Math', 'English', 'Science']
    subject_grades = {subject: [] for subject in subject_names}

    for name, grades in students:
        average_grade = sum(grades) / len(grades)
        print(f"{name}'s average grade: {average_grade:.2f}")

        for i, subject in enumerate(subject_names):
            subject_grades[subject].append(grades[i])

    for subject in subject_names:
        grades = subject_grades[subject]
        highest = max(grades)
        lowest = min(grades)
        print(f"{subject} - Highest grade: {highest}, Lowest grade: {lowest}")


def display_student_summary(students):
    print("\nStudent Summary:")
    for name, grades in students:
        average_grade = sum(grades) / len(grades)
        grades_str = ', '.join(f"{sub}: {grade}" for sub, grade in zip(['Math', 'English', 'Science'], grades))
        print(f"Name: {name}")
        print(f"Grades: {grades_str}")
        print(f"Average Grade: {average_grade:.2f}")
        print()


students = []
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    grades = get_subject_grades()
    students.append((name, grades))

calculate_averages_and_extremes(students)
display_student_summary(students)
