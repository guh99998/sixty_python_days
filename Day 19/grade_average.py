def calculate_average(grades):
    '''
    Calculate the average of a set of grades.

    :param grades: a list of grades to calculate the average.
    :return: the average of the given grades.
    '''
    average = sum(grades) / len(grades)

    return round(average, 2)

print(calculate_average([10, 50, 9620, 56810, 841, 50]))