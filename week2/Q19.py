# 19. Write a function to remove all punctuation from a string.

# import string

# def no_punc(text):
#     return "".join(ch for ch in text if ch not in string.punctuation)

# print(no_punc("Hellooo!!!!!! Madammmmmmm!!!"))

Text = input("Enter the text to remove punctuations in it: ")

def no_punc(Text):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = "".join(ch for ch in Text if ch not in punctuation)
    return result

print(no_punc(Text))
