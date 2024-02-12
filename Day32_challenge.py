# Create a function that calculates the average of a list of numbers

def avg_of_list_of_numbers(my_list):
    sum = 0 
    avg = 0
    for i in range(len(my_list)):
        sum += my_list[i]
    avg = sum/(len(my_list))
    return avg

print(avg_of_list_of_numbers([2,4,6]))