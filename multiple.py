import operator
import functools
import doctest


OPERATION = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def calculate(numbers=None, operator=None):
    """Apply the operator to all numbers, and print result.

    >>> calculate([1, 2, 3, 4], '+')
    10
    >>> calculate([1, 2, 3, 4], '-')
    -8
    >>> calculate([1, 2, 3, 4], '*')
    24
    >>> calculate([120, 2, 3, 4], '/')
    5
    """

    if not numbers:
        amount_of_numbers = int(input("How many numbers? "))
        numbers = [int(input("Number: ")) for _ in range(amount_of_numbers)]

    if not operator:        
        operator = input("Which operator (*, /, +, -)? ")

    result = functools.reduce(OPERATION[operator], numbers)
    print(result)

if __name__ == '__main__':
    doctest.testmod()
    calculate()
