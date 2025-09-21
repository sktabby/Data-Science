# 20. Write a function to capitalize the first letter of each word in a string.

# sentance = input("Enter the strinf to capitalize 1st letter: ")

# def capital(sentance):
#     return sentance.title()

# print(capital(sentance))

# using the manual method for capitalization

sentance = input("Enter the text to capitalize first letter: ")

def capital(sentance):
    capital_next = True
    result=""

    for ch in sentance:
        if ch ==" ":
            result +=ch
            capital_next =True
        else:
            if capital_next:
                if "a"<=ch<="z":
                    ch = chr(ord(ch)-32)
                capital_next=False
            result +=ch
    return result

print(capital(sentance))