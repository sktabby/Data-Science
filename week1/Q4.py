# Create a program that prints the multiplication table of a given number.

n = int(input("Enter the number for the multiplication table: "))
m = int(input("Enter the number of times multiplication should happens: "))

print("Multiplication table of",n)

for i in range(1, m+1):
    print(n,"X",i,"=", n*i)