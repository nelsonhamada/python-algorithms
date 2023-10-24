def is_palindrome_iterative(word):
    if not word:
        return False
    if len(word) == 1:
        return True
    reversed = word[::-1]
    if reversed == word:
        return True
    return False
