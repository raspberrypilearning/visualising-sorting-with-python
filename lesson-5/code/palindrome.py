def find_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return find_palindrome(word[1:-1])
    else:
        return False

if find_palindrome('abcdefedcba'):
    print('Yep')
