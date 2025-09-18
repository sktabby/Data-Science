# Q10. Check if a number is a palindrome.

num = int(input("Enter the palindrom number: "))
original_num= num
reversed_num = 0

while num >0:
    last_digit= num%10
    reversed_num= reversed_num *10 + last_digit
    num //=10


if original_num == reversed_num:
    print(f"{original_num} is palindrome")

else:
    print(f"{original_num} is not palindrome")