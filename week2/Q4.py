# 4. Create a program that removes duplicates from a list.

# method 1 using set()

# numbers= [1,2,3,2,3,2,3,1,4,5,4,5,6]
# unique = list(set(numbers))

# print("The sets of the given list is: ", unique)


# method 2


numbers= [1,2,3,2,3,2,3,1,4,5,4,5,6]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("The sets of the given list is: ", unique)
