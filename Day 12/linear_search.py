def linear_search(list, searched_value):
    '''
    Searches for a number in a list using linear search.

    :param list: a list of numbers.
    :param searched_value: the value to be searched for.
    '''
    for i, number in enumerate(list):
        if number == searched_value:
            return i
    return -1


list = [1,50,55,58,69,508,8568,568,685,850,8,85683,85]
search = 69

search = linear_search(list, search)
print(search)