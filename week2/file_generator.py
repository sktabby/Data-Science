import os

# List of questions
# List of questions
questions = [
    "1. Write a function to check if a number is even.",
    "2. Create a list and find the sum of all its elements.",
    "3. Write a program to find the maximum and minimum in a list.",
    "4. Create a program that removes duplicates from a list.",
    "5. Write a function to reverse a list.",
    "6. Create a tuple and access its elements.",
    "7. Convert a list into a tuple and vice versa.",
    "8. Write a program to merge two dictionaries.",
    "9. Write a function to count the frequency of elements in a list.",
    "10. Create a dictionary of squares of numbers from 1 to 10.",
    "11. Write a program to sort a list in ascending order.",
    "12. Create a program to check if a key exists in a dictionary.",
    "13. Create a set and perform union, intersection, and difference.",
    "14. Write a function to find common elements in two lists.",
    "15. Write a function that returns the factorial of a number.",
    "16. Create a function that checks whether a string is a palindrome.",
    "17. Write a function to count vowels in a string.",
    "18. Create a dictionary and iterate over its keys and values.",
    "19. Write a function to remove all punctuation from a string.",
    "20. Write a function to capitalize the first letter of each word in a string.",
    "21. Create a list comprehension to get squares of all even numbers in a range.",
    "22. Write a function to check if a string is an anagram.",
    "23. Create a nested dictionary to represent student records.",
    "24. Write a function to flatten a nested list.",
    "25. Write a program to find the second highest number in a list.",
    "26. Create a function to rotate a list left by k positions.",
    "27. Write a function to find the missing number from a list of 1 to N.",
    "28. Write a program to remove all None values from a list.",
    "29. Write a function to merge two dictionaries and handle key collisions by summing values.",
    "30. Create a function to find unique elements present in only one of two lists."
]  


# Create files with question commented at the top
base_path = r"C:\Users\Shaikh Tabish\Desktop\pythonnn\week2"
os.makedirs(base_path, exist_ok=True)

for idx, question in enumerate(questions, start=1):
    file_name = f"Q{idx}.py"
    file_path = os.path.join(base_path, file_name)
    with open(file_path, "w") as f:
        f.write(f"# {question}\n\n")

base_path
