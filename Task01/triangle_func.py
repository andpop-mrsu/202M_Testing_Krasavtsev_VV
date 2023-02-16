import doctest


class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(side_a: int, side_b: int, side_c: int) -> str:
    """
    Function for checking type of triangle
    :param side_a: first side of triangle (int)
    :param side_b: second side of triangle (int)
    :param side_c: third side of triangle (int)
    :return: type of triangle (str)
    :raises: IncorrectTriangleSides: if sides was set incorrectly
    >>> get_triangle_type(4, 6, 5)
    'nonequilateral'
    >>> get_triangle_type(4, 4, 4)
    'equilateral'
    >>> get_triangle_type(4, 5, 4)
    'isosceles'
    >>> get_triangle_type(1,'b',3)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect triangle sides: Invalid data type
    >>> get_triangle_type(3, 1, 2)
    Traceback (most recent call last):
     ...
    IncorrectTriangleSides: Incorrect triangle sides: Triangle does not exist
    """


    if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_c, int):
        raise IncorrectTriangleSides('Incorrect triangle sides: Invalid data type')
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        raise IncorrectTriangleSides('Incorrect triangle sides: Triangle does not exist')

    if side_a != side_b and side_a != side_c and side_b != side_c:
        return 'nonequilateral'
    elif side_a is side_b is side_c:
        return 'equilateral'
    else:
        return 'isosceles'


if __name__ == '__main__':
    doctest.testmod()