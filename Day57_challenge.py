# Create a function that returns the key with the maximum value in a dictionary

# create a dictionary 
# walk over the dictionary values 
# find the max value 
# return the key

def return_key_with_max_value(dict):
    max_value = 0
    max_key = ""
    for key in dict:
        # print(key)
        if dict[key] >= max_value:
            max_value = dict[key]
            max_key = key
        else:
            print("This is the end")
    return [max_key ,max_value]


print(return_key_with_max_value({"a":10 , "b": 50 , "c":5}))

