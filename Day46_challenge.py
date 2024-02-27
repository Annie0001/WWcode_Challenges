# Write a function to check if a given list is sorted.


# def check_for_sorted_list(my_list):
#     my_list.sort()
#     return my_list

# print(check_for_sorted_list([1,5,2,10,40,4,0]))


def check_for_sorted_list(my_list):
    copy_of_original_list=my_list.copy()
    new_list=[]

    while my_list:
        minimum = my_list[0]
        for i in my_list:
            if i < minimum:
                minimum = i
        new_list.append(minimum)
        my_list.remove(minimum)
    # return new_list

    if new_list == copy_of_original_list:
        print("This list is sorted.")
    else:
        print("This list is not sorted")

#print(check_for_sorted_list([100,1,2,10,40,4,0]))
print(check_for_sorted_list([1,2,3,4]))