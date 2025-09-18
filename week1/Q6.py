# Convert temperature from Celsius to Fahrenheit.

# celsius = float(input("Enter the temperature in celsius: "))

# fahrenheit = (celsius * 9/5) + 32

# print("Temperature in Fahrenheit is:", fahrenheit)


a = int(input("Enter 1 for Celsius to Fahrenheit And Enter 2 for Fahrenheit to Celsius :"))

if a == 1:
    c=float(input("Enter the Temperature in Celsius: "))
    fahrenheit= (c * 9/5)+32
    print("Temperature in Fahrenheit is:", fahrenheit)

elif a == 2:
    f=float(input("Enter the Temperature in Fahrenheit: "))
    celsius= (5/9)*(f-32)
    print("Temperature in Celsius is:", celsius)

else:
    print("Entered number is not in a range between 1 and 2")


