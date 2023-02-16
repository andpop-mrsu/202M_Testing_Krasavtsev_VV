import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type


class TestTriangleFunction(unittest.TestCase):

    def test_type_error(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, "b", 3)

    def test_incorrect_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 1, 2)

    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(4, 4, 4), 'equilateral')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(4, 6, 5), 'nonequilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(4, '5', 4), 'isosceles')


if __name__ == '__main__':
    unittest.main()