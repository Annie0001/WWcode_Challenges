# Write a program to flatten a nested list

def flatten_list(my_list):
    result=[]
    flatten_list_internal(my_list, result)
    return result

def flatten_list_internal(my_list, result):
    for i in range(len(my_list)):
        if type(my_list[i]) is list:
            flatten_list_internal(my_list[i], result)
        else:
            result.append(my_list[i])



#print(flatten_list([[1], [2, 3], [4, 5, 6, 7]]))
print(flatten_list([[1], [2, 3], [4, 5, 6, 7], [[21,[5,33,11],2]]]))