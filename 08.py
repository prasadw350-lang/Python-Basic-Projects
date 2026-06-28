# Creating Employee class
class Employee:
    # Constructor 
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        # department and salary as a tuple
        self.details = (department, salary)
    # display employee info method
    def show_details(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name :", self.name)
        print("Department :", self.details[0])
        print("Salary :", self.details[1])
# empty dictionary
employees = {}
for i in range(3):
    print(f"\nEmployee {i + 1} Info.")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    try:
        salary = float(input("Salary: "))
        emp = Employee(emp_id, name, department, salary)
        employees[emp_id] = emp
    except ValueError:
        print("Invalid input!")
# Display all employee details
print("\n--- Employee Records ---")
for emp in employees.values():
    emp.show_details()
