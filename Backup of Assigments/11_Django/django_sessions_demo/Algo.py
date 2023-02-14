def count_letters(s):
    count = 0
    for letter in s:
            count += 1
    return count


def count_vowels(s):
    count = 0
    for letter in s:
            if letter.lower() in "aeiuo":
                count += 1
    return count

def count_vowels_dict(s):
    vowels = {
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0,
    }

    for letter in s:
            if letter.lower() in vowels:
                vowels[letter.lower()] += 1
    return vowels






print(count_letters('I love coding'))
print(count_vowels('I love coding'))
print(count_vowels_dict('I love coding'))
