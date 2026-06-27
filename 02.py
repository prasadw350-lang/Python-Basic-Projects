# function
def analyze_string(s):
    if len(s) == 0:
        print("Error: Empty string.")
        return
    # length of the string
    print("Length of String is:", len(s))
    # string in reverse
    print("Reversed String:", s[::-1])
    # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of Vowels:", count)

    #each character with positive and negative index
    print("\nChar\t+ve\t-ve")
    for i in range(len(s)):
        print(s[i], "\t", i, "\t", i - len(s))
# Taking input from the user
text = input("Enter a string: ")
# Calling the function
analyze_string(text)



