# Q28. Write a program to find the sum of all even numbers in a list.


numbers = [1, 2, 3, 4, 5, 6, 10, 15, 20]
sum_even = 0

for n in numbers:
    if n %2 ==0:
        sum_even +=n

print("Sum of even numbers:", sum_even)

