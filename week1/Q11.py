# Q11. Write a program to find the sum of first N natural numbers.


n = int(input("Enter the natural number: "))
total=0

for i in range (1, n+1):
    total+=i

print(f"The sum of first natural {n} is : {total}")