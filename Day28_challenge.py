# Create a program that removes the nth element from a list

# Uneffeicient way of running through the list and finding the index that coresponds to the nth element
# def remove_nth_element(my_list, n):
#     for i in range(len(my_list)):
#         if i == n -1 :
#             my_list.pop(i)
#     return my_list

# pop function removes the item at index n
def remove_nth_element(my_list, n):
    if  n <= len(my_list):
        my_list.pop(n-1)
        return my_list

print(remove_nth_element([1,2,3,4,5,6,7] , 8))
