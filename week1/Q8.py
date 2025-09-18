# Q8. Create a program to count the number of vowels in a string.

text = input("Enter the text: ")
vowels= "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"the number of vowels in the character is {count}")