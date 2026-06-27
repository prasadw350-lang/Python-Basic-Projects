# student database function
def student_database():
    # Empty dictionary
    students = {}
    while True:
        print("\n---Student Database---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            # Add student
            if choice == 1:
                roll_no = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                # update()
                students.update({
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student added successfully.")

            # Search student
            elif choice == 2:
                roll_no = int(input("Enter Roll Number to Search: "))
                # Search using get()
                record = students.get(roll_no)
                if record:
                    print("\nStudent Details")
                    print("Name :", record["Name"])
                    print("Age :", record["Age"])
                    print("City :", record["City"])
                else:
                    print("Student not found.")
            # Display all students
            elif choice == 3:
                if len(students) == 0:
                    print("No student records available.")
                else:
                    print("\nStudent Records")
                    for roll_no, record in students.items():
                        print("------------------------")
                        print("Roll No :", roll_no)
                        print("Name :", record["Name"])
                        print("Age :", record["Age"])
                        print("City :", record["City"])
            # Exit
            elif choice == 4:
                print("Program Ended.")
                break
            else:
                print("Invalid Choice.")
        # invalid input
        except ValueError:
            print("Please enter a valid number.")
# Call the function
student_database()