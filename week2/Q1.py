# 1. Write a function to check if a number is even.


def is_even(number):
    if number %2 ==0:
        return True
    else:
        return False
    
a = int(input("Enter the number to check Even/Odd : "))

print(is_even(a))