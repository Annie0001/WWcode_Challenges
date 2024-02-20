# Write a Python program to check if two strings are anagrams

# Convert both strings to lists of characters.
# Create a dictionary to count the frequency of each character in the first string.
# Iterate over the characters of the second string 
# if it exists in dictionary then decrement the corresponding count in the dictionary.
#    # if the value is 0 then remove the key from dictionary 
# Otherwise say it is not anagram
# check if dictionary is empty then the words are anagram

def anagram_string_check(word_1, word_2):
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
    dict_2 = {}
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

    # for i in range(len(lst_2)):
    #     if lst_2[i] not in dict_2:
    #         dict_2[lst_2[i]] = 1
    #     else:
    #         dict_2[lst_2[i]] += 1
    # print(dict_2)

    # if dict_1[lst_1[i]] in dict_2:
    #     count = dict_1[lst_1[i]] - 1
    #     return count
    # print(count)
    for i in range(len(lst_2)):
        if lst_2[i] in dict_1:
            dict_1[lst_2[i]] = dict_1[lst_2[i]] - 1
        # return dict_1[lst_1[i]]
    
    # print ("This words are anagram")
    print(dict_1)
print(anagram_string_check("A gentleman","Elegant man"))
# print(anagram_string_check("gentleman","Elegant man"))