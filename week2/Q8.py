# 8. Write a program to merge two dictionaries.

# method 1 using update

# dict1={"a":1 , "b":2}
# dict2={"c":3 , "d":4}

# dict1.update(dict2)
# print(dict1)

# Method 2: using {**dict1, **dict2}

dict1={"a":1 , "b":2}
dict2={"c":3 , "d":4}

dict3 = { **dict1, **dict2}

print(dict3)