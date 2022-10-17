
def pig_latin(*words, suffix = "ay", single = False):
    ''' function to do latin stuff ...'''

    # split up any word in a list!
    sub_words= []
    for sub in words:
        sub_words.append(sub.split())

    # flatten all list!
    try:
        all_words = [element for sublist in sub_words for element in sublist]
    except TypeError:
        all_words = sub_words[:]

    # define the vowels
    vowel = ["a", "e", "i", "o", "u"]

    # loop over all words!
    for index, word in enumerate(all_words):
        if str(word)[0].lower() in vowel:
            all_words[index] += suffix
        else:
            newword = str(str(word)[1:] + str(word)[0]).capitalize()
            all_words[index] = newword  + suffix

    if single == False:
        return all_words
    else:
        return " ".join(all_words)


### Test cases
test1_data = ["Word", "Apple"]
test1_config = {}
test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}
test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))
print(pig_latin(*test2_data, **test2_config))
print(pig_latin(*test3_data, **test3_config))