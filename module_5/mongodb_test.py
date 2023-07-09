students = []  # Create an empty list called 'students'

# Function to add a student to the list
def add_student():
    name = input("Enter the student's name: ")
    students.append(name)
    print("Student added successfully!")

# Main program loop
while True:
    print("1. Add a student")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")

# End of the program
input("Press any key to exit.")

