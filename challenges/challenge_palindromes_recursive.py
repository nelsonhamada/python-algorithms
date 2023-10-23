def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if high_index >= 3 and word[low_index] == word[high_index]:
        wordSliced = word[(low_index + 1): high_index]
        return is_palindrome_recursive(wordSliced, 0, len(wordSliced) - 1)
    if high_index >= 0 and word[low_index] == word[high_index]:
        return True
    return False
