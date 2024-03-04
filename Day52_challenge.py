# Create a program that checks if a string is a palindrome

# go over the string from left to right 
# go over the same string from the right to left
# check if the left to right and the right to left readings are equal

def check_palindrome(my_string):
    if my_string[:] == my_string[::-1]:
        # return my_string
        print("This word is palindrom")
    else:
        print("This word is Not Palindrom")

# check_palindrome("wow")
check_palindrome("Aren")