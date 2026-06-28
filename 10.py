# Importing modules
import math
import random
from datetime import datetime

# Dictionary to store history
history = {}
def arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Choose Operation: "))
        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            result = num1 / num2
        else:
            print("Invalid Choice")
            return
        print("Result =", result)
        # result with timestamp
        history[str(datetime.now())] = result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid Input.")

def scientific():
    try:
        number = float(input("Enter Number: "))
        print("Square Root =", math.sqrt(number))
        print("Square =", math.pow(number, 2))
        print("Factorial =", math.factorial(int(number)))
        history[str(datetime.now())] = {
            "Square Root": math.sqrt(number),
            "Square": math.pow(number, 2),
            "Factorial": math.factorial(int(number))
        }
    except ValueError:
       print("Enter a valid positive number.")
    except Exception as e:
        print("Error:", e)

def random_numbers():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(1, 100))
    print("Random Numbers:", numbers)
    history[str(datetime.now())] = numbers

def view_history():
    if len(history) == 0:
        print("No History Available.")
    else:
        print("\nCalculation History")
        for time, value in history.items():
            print(time, ":", value)

while True:
    print("\n--- Smart Calculator & Data Manager ---")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")
    try:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            arithmetic()
        elif choice == 2:
            scientific()
        elif choice == 3:
            random_numbers()
        elif choice == 4:
            view_history()
        elif choice == 5:
            print("Program Ended.")
            break
        else:
            print("Invalid Choice.")
    except ValueError:
        print("Please enter a valid number.")
