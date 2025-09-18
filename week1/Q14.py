# Q14. Check if a given year is a leap year or not.

year = int(input("Enter the year: "))

if (year % 400 ==0) or (year % 100 != 0 and year % 4 ==0):
    print("The entered year is leap year")

else:
    print("The enteres year is not leap year")