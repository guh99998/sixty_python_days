def is_palindrome(text):
    '''
    Verify if a word or phrase is a palindrome.

    :param text: a word, text or number.
    :return: true if the input is a palindrome, false otherwise.
    '''
    text = str(text).replace(" ", "").lower()

    if text == text[::-1]:
        return f'{text} is a palindrome.'
    return f'{text} is not a palindrome.'


print(is_palindrome('ovo'))