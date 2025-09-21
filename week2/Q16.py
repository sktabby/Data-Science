# 16. Create a function that checks whether a string is a palindrome.
s = input("Enter the Text to check :")
def palindrom(s):
    s = s.upper()
    return s==s[::-1]

print(palindrom(s))