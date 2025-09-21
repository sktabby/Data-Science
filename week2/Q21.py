# 21. Create a list comprehension to get squares of all even numbers in a range.

# even_square = [x**2 for x in range(1,11) if x %2 ==0]
# print(even_square)

# for input range

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

e_square = [x**2 for x in range(start, end+1) if x %2 ==0]
print(e_square)