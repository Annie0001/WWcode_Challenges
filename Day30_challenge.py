# Create a function that finds the second smallest element in a list.

######## Finds just the smallest elemet ########
# def find_second_smallest_element(my_list):
#     smallest_element = my_list[0]
#     for i in range(len(my_list)):
#         if my_list[i] <= smallest_element:
#             smallest_element = my_list[i]
#     return smallest_element

######## Using built in function sort ########
# def find_second_smallest_element(my_list):
#     my_list.sort()
#     return my_list[1]

def find_second_smallest_element(my_list):
    smallest_element = my_list[0]
    second_smallest_element = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] <= smallest_element:
            smallest_element = my_list[i]
        elif my_list[i] <= second_smallest_element:
            second_smallest_element = my_list[i]

    return smallest_element , second_smallest_element


print(find_second_smallest_element([10,30,8,13,14,15]))





