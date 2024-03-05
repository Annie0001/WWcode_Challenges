# Create a function to find all words in a sentence that start with a vowel

# have a list for vowels
# split the given sentence into separate words in a list
# loop through the word list and check if any of the words starts with any of the items in the vowels list
# Then print that word

def start_with_vowel_words(my_string):
    my_string = my_string.lower()
    
    vowel_list = ["a", "e", "i", "o", "u", "y", "w"]
    #txt = "hello, my name is Peter, I am 26 years old"
    # x = txt.split(", ")
    words_list = my_string.split(" ")
    print(words_list)
    for word in words_list:
        for vowel in vowel_list:
            if word[0] == vowel:
                print(word)


start_with_vowel_words("It is a sunny day.")