# function
def manage_marks():
    marks = []
    while len(marks) < 5:
        try:    
            mark = float(input("Enter marks of 5 subjects:"))
            marks.append(mark)
        except ValueError:
            print("Error: Please enter a valid numeric value.")
    
    # Calculates and prints the average, highest, and lowest marks.
    print("Marks List:", marks)
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    # Sorting the list in descending order
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)
# Call function
manage_marks()