'''Two words are “rotate pairs” if you can rotate one of them and get the other
Write a program that reads a wordlist and finds all the rotate pairs.

Stuff to know: ord('c') => number
               chr(n)   => Character
'''

# import string library function 
import string 
    
def rotate_word(word: str, n: int) -> str:
    '''Rotate/Shift any character of a word by {n}'''

    # define rotated_word
    rotated_word = ""
    for char in word:
        # validate character
        if char in string.ascii_lowercase or char in string.ascii_uppercase:
            if 65 <= ord(char)<= 90:
                # check if uppercase
                min_ascii_value = 65
                max_ascii_value = 90
            elif 97<= ord(char)<= 122:
                # check if lowercase
                min_ascii_value = 97
                max_ascii_value = 122
            else:
                # invalid character (2nd check!), might be useless
                continue
            
            # calculate amount of shift
            shift = ord(char) + n
            if shift < min_ascii_value:
                # round robin if < min ascii
                shift = max_ascii_value - min_ascii_value - shift
            if shift > max_ascii_value:
                # round robin if > max ascii
                shift = min_ascii_value-1 + shift - max_ascii_value
            # rebuild shifted word
            rotated_word += chr(shift)
    return rotated_word


######   main program ######

word_list = ["This","was","sent","in","by","a","fellow","named","Dan", "stuff",
             "Ure", "pcogf", 'q', "z", 'ty', 'Bpqa', 'amvb', 'mlssvd', 'Ebo', "some", "other", "mnozz"]

# define main dictionary
cipher_dict = {}
for word in word_list:
    # define sub dictionary
    word_dict = {}
    for amount_of_shift in range(1,26):
        if rotate_word(word,amount_of_shift) in word_list:
            # update sub dictionary if cipher is in word_list
            word_dict.update({rotate_word(word,amount_of_shift):amount_of_shift})
    # update main dictionary for every word
    cipher_dict.update({word: word_dict})
# print result
for word in cipher_dict:
    print(f"For word: {word:>6} i found these ciphers rotated word ciphers {cipher_dict[word]}")
