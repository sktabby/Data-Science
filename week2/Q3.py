# 3. Write a program to find the maximum and minimum in a list.


numbers = [74, 00, 41, 77, 31]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum= num
    if num < minimum:
        minimum= num

print("Maximum: ", maximum)
print("Minimum: ",minimum)