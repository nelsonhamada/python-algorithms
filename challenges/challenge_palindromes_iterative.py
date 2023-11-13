def is_palindrome_iterative(word):
    if not word:
        return False
    return word[::-1] == word
