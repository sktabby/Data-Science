# Q16. Write a program to find the GCD of two numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b !=0:
    a,b = b, a%b

print("GDC is:", a)