# Creating Student class
class Student:
    # Constructor 
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    # add marks method
    def add_mark(self, mark):
        try:
            mark = float(mark)
            # Check if marks are valid
            if mark < 0 or mark > 100:
                raise ValueError
            self.marks_list.append(mark)
        except ValueError:
            print("Invalid mark!")

    # calculate average method
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    # Method to display student information
    def display_info(self):
        print("\n--- Student Details ---")
        print("Name :", self.name)
        print("Roll Number :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())


# Taking student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
# student object
student = Student(name, roll_no)
# 5 subjects marks
print("\nEnter marks for 5 subjects:")
for i in range(5):
    mark = input(f"Subject {i + 1}: ")
    student.add_mark(mark)
# Display 
student.display_info()