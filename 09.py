# Import math module
import math
try:
    # Taking sentence as input
    sentence = input("Enter a sentence: ")
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    # sentence into words
    words = sentence.lower().split()
    # Store words in set
    unique_words = set(words)
    # Display unique words in sorted order
    print("\nSorted order:")
    for word in sorted(unique_words):
        print(word)
    total = len(unique_words)
    # Print square (raised to the power 2)
    print("\nTotal Unique Words:", total)
    print("Square of Total Unique Words:", math.pow(total, 2))
# Exception handling
except ValueError :
    print("Error:", ValueError)
except Exception as e:
    print("Unexpected Error:", e)
