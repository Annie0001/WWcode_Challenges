# Create a program that checks if a given string is a valid email address.


############## Solved with built-in Regex function #######################
# import re

# email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

# def is_valid_email(email):

#     return email_regex.match(email) is not None

# print(is_valid_email("aaa@gmail.com"))
# print(is_valid_email(" "))



############## Manually validating an Email Address #######################
def is_valid_email_2(email):
    # check email if it has @
    # then split with @
    # the list should have 2 elements.if yes continue, else return false
    # then take second element and check if it has ., else return false
    # then take second element and split with .
    # if the list has 2 elements then return true else return false
    
    if "@" in email: 
        address = email.split("@")
        if len(address) == 2 and address[0] != "": 
            print(address)
            print("It has 2 elements")
            if "." in address[1]:
                print("It has . ")
                second_element = address[1].split(".")
                print(second_element)
                if len(second_element) == 2 and second_element[0] != "" and second_element[1] != "":
                    print("it has 2 elements after @sign")
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else: 
        return False



# print(is_valid_email_2("aaa@gmail.com"))
# print(is_valid_email_2("aaagmail.com"))
#print(is_valid_email_2("@gmail.com"))
#print(is_valid_email_2("aaa@.com"))
print(is_valid_email_2("aaa@gmail."))
