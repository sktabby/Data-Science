# Q22. Create a program to print all Armstrong numbers between 1 to 1000.

print("Enter the number for armstrong calculation")

for num in range(1, 1001):
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)

    if total == num:
        print(num , end=" ")