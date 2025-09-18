# Q15. Create a program to print the Fibonacci series up to N terms.

n = int(input("Enter the number for fibonacci series"))

a, b = 0, 1

print("Fibonacci series")

for i in range(n):
    print(a, end=" ")

    a,b=b, a+b