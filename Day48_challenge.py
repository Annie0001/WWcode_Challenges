# Create a program that replaces specific words in a text with their synonyms

# example: This sofa is very comfortable. 
# synonym for comfortable = snug or cozy

# 1.have a dictionary of synonyms
# 2.convert the text into the list of words
# 3.walk through the list of words from the text and find the words that are the same as the keys in the synonyms dictionary
# 4.Once the matching word is found then replace it in the text list with the matching value of the key from the synonyms dictionary


synonyms = {"beautiful":"pretty" , "comfortable":"snug", "organized":"arranged"}

my_text = "This is a very comfortable sofa with beautiful color. Your dining area is also very organized."

# def replace_words_with_synonyms(my_text):
#     text_list =[]
#     result_text_list=[]
#     text_list = my_text.split(" ")
#     print(text_list)
#     for item in text_list:
#         # print(item)
#         if item in synonyms:
#             # item = synonyms[item]
#             result_text_list.append(synonyms[item])
#         else:
#             result_text_list.append(item)
#     print(result_text_list)

# replace_words_with_synonyms(my_text)

#####################################################


def replace_words_with_synonyms(my_text):
    text_list =[]
    result_text_list = ""
    text_list = my_text.split(" ")
    print(text_list)
    for item in text_list:
        # print(item)
        if item in synonyms:
            # item = synonyms[item]
            result_text_list += synonyms[item] + " "
        else:
            result_text_list += item + " "
    print(result_text_list)

replace_words_with_synonyms(my_text)