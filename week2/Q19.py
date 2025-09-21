# 19. Write a function to remove all punctuation from a string.

import string

def no_punc(text):
    return "".join(ch for ch in text if ch not in string.punctuation)

print(no_punc("Hellooo!!!!!! Madammmmmmm!!!"))

