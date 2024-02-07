# Create a program that uses a lambda function to square each element of a list.

x = lambda a: a * a
def square_elements_of_list(my_list):
    
    for i in range(len(my_list)):
        my_list[i] = x(my_list[i])

    return my_list

print(square_elements_of_list([2,3,4]))