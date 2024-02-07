#   Create a program to concatenate two lists.

def list_concat(list_one, list_two):

    list_one.extend(list_two)
    return list_one

print(list_concat([1,2,3],[4,5,6]))
