class Student:
    def __init__(self, name):
        """Initialize a student with a name and an empty dictionary of grades."""
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add or update the grade for a subject."""
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def calculate_average(self):
        """Calculate the average grade for the student."""
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0

    def print_details(self):
        """Print the student's details including their grades and average."""
        grades_str = ', '.join(f"{subject}: {grade}" for subject, grade in self.grades.items())
        average_grade = self.calculate_average()
        print(f"Name: {self.name}")
        print(f"Grades: {grades_str}")
        print(f"Average Grade: {average_grade:.2f}")


class Gradebook:
    def __init__(self):
        """Initialize a Gradebook with an empty collection of students."""
        self.students = {}

    def add_student(self, name):
        """Add a new student to the gradebook."""
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print(f"Student {name} already exists.")

    def remove_student(self, name):
        """Remove a student from the gradebook."""
        if name in self.students:
            del self.students[name]
            print(f"Student {name} has been removed.")
        else:
            print(f"Student {name} does not exist.")

    def search_student(self, name):
        """Search for a student by name and print their details."""
        if name in self.students:
            self.students[name].print_details()
        else:
            print(f"Student {name} not found.")

    def add_student_grade(self, name, subject, grade):
        """Add or update the grade of a student for a specific subject."""
        if name in self.students:
            try:
                self.students[name].add_grade(subject, grade)
            except ValueError as e:
                print(e)
        else:
            print(f"Student {name} not found.")

    def calculate_averages_and_extremes(self):
        """Calculate and print the highest and lowest grades per subject."""
        subject_names = ['Math', 'English', 'Science']
        subject_grades = {subject: [] for subject in subject_names}

        for student in self.students.values():
            for subject in subject_names:
                if subject in student.grades:
                    subject_grades[subject].append(student.grades[subject])

        for subject, grades in subject_grades.items():
            if grades:
                highest = max(grades)
                lowest = min(grades)
                print(f"{subject} - Highest grade: {highest}, Lowest grade: {lowest}")

    def sort_students_by_average(self):
        """Sort and display students by their average grade."""
        sorted_students = sorted(self.students.values(), key=lambda s: s.calculate_average(), reverse=True)
        print("\nStudents sorted by average grade:")
        for student in sorted_students:
            student.print_details()

    def sort_students_by_subject(self, subject):
        """Sort and display students by a specific subject's grade."""
        sorted_students = sorted(
            [student for student in self.students.values() if subject in student.grades],
            key=lambda s: s.grades[subject], reverse=True
        )
        print(f"\nStudents sorted by {subject} grade:")
        for student in sorted_students:
            student.print_details()


# Testing the Gradebook System

def main():
    gradebook = Gradebook()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add/Update Student Grade")
        print("4. Search Student")
        print("5. Calculate Averages and Extremes")
        print("6. Sort Students by Average Grade")
        print("7. Sort Students by Subject Grade")
        print("8. Exit")

        option = input("Select an option: ")
        if option == '1':
            name = input("Enter the student's name: ")
            gradebook.add_student(name)
        elif option == '2':
            name = input("Enter the student's name to remove: ")
            gradebook.remove_student(name)
        elif option == '3':
            name = input("Enter the student's name: ")
            subject = input("Enter the subject: ")
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                gradebook.add_student_grade(name, subject, grade)
            except ValueError:
                print("Invalid grade input. Please enter a numeric value.")
        elif option == '4':
            name = input("Enter the student's name to search: ")
            gradebook.search_student(name)
        elif option == '5':
            gradebook.calculate_averages_and_extremes()
        elif option == '6':
            gradebook.sort_students_by_average()
        elif option == '7':
            subject = input("Enter the subject to sort by: ")
            gradebook.sort_students_by_subject(subject)
        elif option == '8':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
