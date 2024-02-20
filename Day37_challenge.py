# Write a program to iterate through a dictionary and print its keys and values

def key_and_value(dict):
    for key, value in dict.items():
        print (key , value)

print(key_and_value({'a':1, 'b':2 , 'c': 4}))