def factorial(n):
    '''
    Calculates the factorial of a number using recursion.

    :param n: an integer number.
    :return: the factorial of n.
    '''
    if n < 0:
        raise ValueError('Invalid input')
    
    if n == 0 or n==1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(3))