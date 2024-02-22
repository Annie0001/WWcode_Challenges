# Write a program to find the most common words in a text file

def find_most_common_words():
    dict ={}
    # openning a text file
    File_object = open(r"first_text_file.txt")
    while True:
        # Reads a line of the file and returns in form of a string.
        line = File_object.readline()
        if not line:
            break
        line = line.strip()
        # print(line)
        if line not in dict:
            dict[line]= 1
        else: 
            dict[line] = dict[line] + 1
    print(dict)
    max_value = 0
    max_key = ""
    for key, value in dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key



        

    #  Reads a line of the file and returns in form of a string.
    #  For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.
    #  File_object.readline([n])
    # File_object.readline()


    File_object.close()

print(find_most_common_words())