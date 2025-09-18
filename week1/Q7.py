# Write a program to calculate the factorial of a number using a loop.

num = int(input("Enter the number for factorial: "))
factorial = 1

if num < 0:
    print("Factorial doesn't exist for negative number")

elif num ==0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial*=i
        # print(factorial)
        print(f"The factorial of {num} is {factorial}.")
