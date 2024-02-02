# Write a program that checks if a key exists in a dictionary.
def key_exists(dic_list, key):

    if key in dic_list:
        return dic_list[key]
            
print(key_exists({"num1": 1,"num2": 2,"num3": 3},"num1"))
