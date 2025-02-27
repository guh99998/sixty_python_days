def anagram(word_1, word_2):
    '''
    Checks if two words are anagrams.

    :param word_1: The first word.
    :param word_2: The second word.
    :return: True if the words are anagrams, False otherwise.
    '''
    word_1 = word_1.replace(" ", "").lower()
    word_2 = word_2.replace(" ", "").lower()

    if sorted(word_1) == sorted(word_2):
        return f'The words are anagrams'
    return f'The words are not anagrams'


print(anagram('car', 'bus'))