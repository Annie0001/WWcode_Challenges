# Create a program that finds the intersection and union of two sets

# Union        -    A={1,2,3} ,B={3,4,5} - A U B = {1,2,3,4,5}
# Intersection -    x = {"apple","banana","cherry"} , y={"google","microsoft","apple"} Intersection = {"apple"}

# create a new empty list
# iterate over the first list and add the items one by one to the new list
# iterate over the second list and add the items that are not repeated in the first list to the new list as well.

# In order to skip having 2 for loops, just walk over the second list and append it to the first list.

###################  Union ###########################
# def find_union_for_two_sets(list_1, list_2):
#     # results_list = []
#     # for i in range(len(list_1)):
#     #     results_list.append(list_1[i])
    
#     # for j in range(len(list_2)):
#     #     if list_2[j] not in list_1:
#     #         results_list.append(list_2[j])
#     # return results_list
#################################################
#     for i in range(len(list_2)):
#         if list_2[i] not in list_1:
#             list_1.append(list_2[i])        
#     return list_1

# print(find_union_for_two_sets([1,2,3],[3,4,5]))

################# Intersection ###########################

def find_intersection_for_two_sets(list1, list2):
    result = []
    for i in range(len(list2)):
        if list2[i] in list1:
            result.append(list2[i])
    return result
# print(find_intersection_for_two_sets([1,2,3],[3,4,5]))
# print(find_intersection_for_two_sets([1,2,3,4],[3,4,5]))
print(find_intersection_for_two_sets([1,2,3,4],[3,4,5,2]))