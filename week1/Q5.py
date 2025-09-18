# Write a program to find the largest of three numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))

if a>b and a>c :
    print("First number is the largest number which is:", a)
elif b>a and b>c :
    print("First number is the largest number which is:", b)
elif c>a and c>b :
    print("First number is the largest number which is:", c)
else:
    print("All entered numbers are equal:", a)