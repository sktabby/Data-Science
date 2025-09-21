# 17. Write a function to count vowels in a string.

s= input("Enter the Text to count the vowels: ")

def c_v(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if  ch in vowels:
            count +=1
    return count

print("Count of vowels is: ", c_v(s))