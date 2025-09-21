# 14. Write a function to find common elements in two lists.

def common_list(list1, list2):
    return list(set(list1)& set(list2))

print(common_list([1,2,3,4,5,6], [3,4,5,6,7,8]))