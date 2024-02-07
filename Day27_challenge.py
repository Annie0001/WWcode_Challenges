# Create a program that sorts a list of strings alphabetically.

# Without input from user
# def alphabetic_list_sort(my_list):
#     # for item in my_list:
#     return sorted(my_list)

# print(alphabetic_list_sort(["Apple","Cold","Bag","Door"]))

# With user input
list_of_strings = []
for i in range(5):
    string = input('Enter a string: ')
    list_of_strings.append(string)
list_of_strings.sort()
print(list_of_strings)
