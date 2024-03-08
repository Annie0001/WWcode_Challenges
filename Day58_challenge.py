# Create a function that converts a string to an integer and handles ValueError

# string - "1001"
# integer - 1001

# print(type("1001"))
# print(int("1001"))

def convert_string_to_integer(str):
    try: 
        integer_type = int(str)
        # print(type(integer_type))
        return integer_type
    except:
        print("You provided a wrong value. Please enter an integer!")

# print(convert_string_to_integer("1001"))
someInt = convert_string_to_integer("aren")
if someInt is not None:
    print(someInt)

convert_string_to_integer("")