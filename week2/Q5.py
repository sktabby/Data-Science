# 5. Write a function to reverse a list.

#Method 1 using slicing  ::-1

# numbers = [10,20,30,40,50]

# def reverse_list(ist):
#     return ist[::-1]
# print(reverse_list(numbers))

# Method 2 using loop

numbers = [10,20,30,40,50]
reverse_list = []

for num in numbers:
    reverse_list.insert(0,num)

print(reverse_list)