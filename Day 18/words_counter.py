def words_counter(text):
    '''
    Count the number of words in a string.

    :param text: The input string.
    :return: The number of words in the string.
    '''
    words = text.split()

    return len(words)

print(words_counter('testando o contador de palavras'))