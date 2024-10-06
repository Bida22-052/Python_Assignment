# Function to validate grade input
def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter the student's grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main program
def main():
    # Prompt the user for the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students in the class: "))
            if num_students > 0:
                break
            else:
                print("Number of students must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Initialize an empty list to store student data
    students = []

    # Loop to collect data for each student
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        grade = get_valid_grade()
        students.append((name, grade))  # Store each student's name and grade as a tuple

    # Calculate total and average grades
    total_grade = sum(grade for _, grade in students)
    average_grade = total_grade / num_students if num_students > 0 else 0

    # Display each student's name and grade
    print("\nStudent Grades:")
    for name, grade in students:
        print(f"{name}: {grade:.2f}")

    # Display the class average
    print(f"\nTotal Grade: {total_grade:.2f}")
    print(f"Class Average Grade: {average_grade:.2f}")

# Run the program
if __name__ == "__main__":
    main()
