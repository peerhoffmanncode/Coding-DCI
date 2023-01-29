def is_palindrome(string: str):
    return string == string[::-1]


def rec_is_palindrome(string: str):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return rec_is_palindrome(string[1:-1])
    else:
        return False


print(rec_is_palindrome('aba'))     # True
print(rec_is_palindrome('abba'))    # True
print(rec_is_palindrome('abcba'))   # True

print(rec_is_palindrome('abc'))     # False
print(rec_is_palindrome('abbb'))    # False
print(rec_is_palindrome('abab'))    # False
