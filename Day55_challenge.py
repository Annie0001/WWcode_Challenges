# Create a function that takes a string and returns the reverse of each word
# eg "This is my House"
# output: siht si ym esuoh

# take the string and lower case it
# split the sentance into words list.
# go over each word in the list
# then reverse it and print it out


def reverse_each_word_in_string(str):
    reversed_string = ""
    sentance = str.lower()
    # print(sentance)
    word_list = sentance.split(" ")
    print(word_list)
    for word in word_list:
        # print(word[::-1])
        reversed_word = " "
        for letter in word:
            reversed_word = letter + reversed_word
        print(reversed_word)

        reversed_string = reversed_string + reversed_word

    print(reversed_string)
        



reverse_each_word_in_string("This is my House")