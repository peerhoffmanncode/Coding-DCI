def rec_is_palindrome(string: str):
    string = string.replace(" ", "")
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return rec_is_palindrome(string[1:-1])
    else:
        return False


print(rec_is_palindrome('aba'))     # True
print(rec_is_palindrome('ab   a'))    # True
print(rec_is_palindrome(' a z  a'))   # True

print(rec_is_palindrome('ab a b'))     # False
print(rec_is_palindrome('a a  ba'))    # False
print(rec_is_palindrome('a z a a'))    # False
