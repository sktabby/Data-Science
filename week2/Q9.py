# 9. Write a function to count the frequency of elements in a list.


def c_f(list_item):
    freq ={}
    for item in list_item:
        if item in freq:
            freq[item] +=1
        else:
            freq[item] =1

    return freq

numbers = [1,2,1,2,3,3,4,5,5,5, 99]

print(c_f(numbers))