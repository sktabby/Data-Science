# 15. Write a function that returns the factorial of a number.


n = int(input("Enter the number for the factorial: "))

def fact(n):
    result =1
    for i in range(1,n+1):
            result *=i
    return result

print("The factorial of number",n, "is", fact(n))