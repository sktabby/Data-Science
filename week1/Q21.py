# Q21. Write a program to count the number of digits in an integer.


num = int(input("Enter the number to count the digit"))
count = 0


while num >0 :
    count +=1
    num //=10

print("Number of digits are ", count)