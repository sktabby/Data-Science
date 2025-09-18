# Q17. Write a program to find the LCM of two numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


def gcd(x,y):
    while y!=0:
        x,y = y, x%y
    return x


lcm = (a*b) // gcd(a,b)

print("LCM is: ", lcm)