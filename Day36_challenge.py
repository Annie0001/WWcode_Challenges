# Write a Python program to check if two strings are anagrams

# Convert both strings to lists of characters.
# Create a dictionary to count the frequency of each character in the first string.
# Iterate over the characters of the second string 
# if it exists in dictionary then decrement the corresponding count in the dictionary.
#    # if the value is 0 then remove the key from dictionary 
# Otherwise say it is not anagram
# check if dictionary is empty then the words are anagram

def anagram_string_check(word_1, word_2):
    if len(word_1) != len(word_2):
        print("These two words are not anagram")
        return
    first_word = word_1.lower()
    second_word = word_2.lower()
    lst_1 = []
    lst_2 = []
    #split a string into a list of characters
    lst_1[:]= first_word
    lst_2 [:] = second_word

    print(lst_1)
    print(lst_2)

    dict_1 = {}
    # dict_2 = {}
    # dict_1 = {
    #    'a' : 2,
    #    'e' : 2,
    #    'm' : 1
    # }
    
    count = 0
    for i in range(len(lst_1)):
        #dict_1[lst_1[i]] = 1
        # check if key exists in dict_1
        if lst_1[i] not in dict_1:
            dict_1[lst_1[i]] = 1
        else:
            dict_1[lst_1[i]] += 1
    print(dict_1)

    for i in range(len(lst_2)):
        if lst_2[i] in dict_1:
            dict_1[lst_2[i]] = dict_1[lst_2[i]] - 1
            if dict_1[lst_2[i]] == 0:
                dict_1.pop(lst_2[i])
        else:
            print ("This words are Not anagram")
            return
    
    print(dict_1)
    if len(dict_1) == 0:
        print ("This words are anagram")
    else:
        print ("This words are Not anagram")


# anagram_string_check("A gentleman","Elegant man")
anagram_string_check("gentleman","Elegant man")