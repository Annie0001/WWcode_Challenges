# Write a program that removes all whitespaces from a given string

# method 1 - using strip function
# def remove_whitespaces(my_string):

#     no_space = my_string.replace(" ","")
#     print(no_space)

# remove_whitespaces("A cute dog")


# method 2 - using strip function
def remove_whitespace_from_string(str):
    str_storage = ""
    for i in range(len(str)):
        if " " != str[i]:
            str_storage += str[i]
    return str_storage

print(remove_whitespace_from_string("A cute dog"))
