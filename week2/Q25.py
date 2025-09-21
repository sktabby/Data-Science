# 25. Write a program to find the second highest number in a list.

# numbers = [5, 2, 9, 1, 7]
# numbers.sort(reverse=True)
# print(numbers[1])



numbers = [5, 2, 9, 1, 7]

first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second higher number is :", second)

