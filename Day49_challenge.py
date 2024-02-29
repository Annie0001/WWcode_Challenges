# Create a program that implements the bubble sort algorithm


def bubble_sort_algo(my_list):
    n= len(my_list)
    for i in range(n):
        for j in range(0,n-1):
            if my_list[j]>my_list[j+1]:
                # swap(my_list[j],my_list[j+1])
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort_algo([10,13,2,9,4]))
