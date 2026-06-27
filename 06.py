# Import modules
import random
import math
try:
    # creating empty set
    numbers = set()
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i + 1}: "))
        numbers.add(num)
    print("\nUnique Numbers:", numbers)
    # Convert set to tuple
    numbers_tuple = tuple(numbers)
    print("Tuple:", numbers_tuple)
    # least 3 elements must be in tuple
    if len(numbers_tuple) >= 3:
        # 3 random unique numbers
        random_numbers = random.sample(numbers_tuple, 3)
        print("3 Random Numbers:", random_numbers)
    else:
        print("Not enough unique numbers to select 3.")
    # sum 
    total = sum(numbers_tuple)
    # square root of sum
    print("Square Root of Sum:", math.sqrt(total))
# Exception handling
except ValueError:
    print("Please enter valid integer values.")
except Exception :
    print("Error:", Exception)