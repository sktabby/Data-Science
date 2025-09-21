# 12. Create a program to check if a key exists in a dictionary.

key = input("Enter the key to check if its exist: ")

student = {"name": "Ali", "age": 20, "grade": "A"}

if key in student:
    print("Key exist")
else:
    print("Key does not exist")