# Write a program to remove vowels from a given string.

vowel_list=["A","E","I","O","U","a","e","i","o","u"]
def remove_vowel(word):
    for i in vowel_list:
        if i in word:
            word = word.replace (i,"")
    return word

print(remove_vowel("forget"))