# Create a program that checks if a string is a palindrome

# go over the string from left to right 
# go over the same string from the right to left
# check if the left to right and the right to left readings are equal

##################### Used Slicing #########################

# def check_palindrome(my_string):
#     if my_string[:] == my_string[::-1]:
#         # return my_string
#         print("This word is palindrom")
#     else:
#         print("This word is Not Palindrom")

# # check_palindrome("wow")
# check_palindrome("Aren")


##################### Character By Character comparison Using Indices ###############

# Read from left to right character by characte and compare each character with the same position character when reading from right to left
# If the characters are same then continue to the next index comparison
# If it is not equal then just print Not Palindrom
# Once the loop finishes and all characters are equal, then say it is palindrom

def check_palindrome(my_string):

    #print(my_string[0])
    #print(my_string[-1])
    #print(my_string[-2])
    #print(my_string[len(my_string)-1])

    i = 0
    j = len(my_string) -1

    # Moving forward with i 
    # Moving backwards with j
    while i < j:
        if my_string[i] == my_string[j]:
            i=i+1
            j=j-1
        else:
            print("This word is Not Palindrom")
            return
    print("This word is Palindrom")
    
# check_palindrome("wow")
check_palindrome("wowtr")