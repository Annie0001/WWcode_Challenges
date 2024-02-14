# Write a Python program to merge two dictionaries

########## Using update built in function ##########
# def merge_two_dictionaries(dict_1, dict_2):
#     dict_1.update(dict_2)
#     return dict_1


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# fruit = {
#   "fruit": "Apple",
#   "color": "Red",
#   "taste":"Sweet"
# }
# print(merge_two_dictionaries(car, fruit))

######### Adding the seond dictionary to the first one
######### by iterating through the second dictionary 
######### and adding the key, value pairs to the first dictionary
def merge_two_dictionaries_2(dict_1, dict_2):
    for key, value in dict_2.items():
        dict_1[key] = value
    return dict_1


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
fruit = {
  "fruit": "Apple",
  "color": "Red",
  "taste":"Sweet"
}
print(merge_two_dictionaries_2(car, fruit))

