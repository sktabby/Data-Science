# Q20. Create a program to find the second largest number in a list.



numbers = [10, 40, 77, 30, 50]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest= largest
        largest= num
    elif num > second_largest and num != largest:
        second_largest= num
print("The second largest number is ", second_largest)