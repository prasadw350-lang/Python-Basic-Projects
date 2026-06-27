try:
    #lambda function 
    square = lambda x: x * x
    # empty list
    squares = []
    # Generate numbers from 1 to 20
    for num in range(1, 21):
        squares.append(square(num))
    # Display squares
    print("Squares of numbers from 1 to 20:")
    print(squares)
    # Prints only even squares
    print("\nEven Squares:")
    for value in squares:
        if value % 2 == 0:
            print(value, end=" ")
# Handle unexpected errors
except Exception as e:
    print("Error:", e)
