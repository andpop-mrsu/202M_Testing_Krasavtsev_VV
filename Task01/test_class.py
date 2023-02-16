import pytest
from Triangle import Triangle
from triangle_func import IncorrectTriangleSides


class TestTriangleClass:
    def test_triangle_create(self):
        triangle = Triangle(4, 6, 5)
        assert triangle.side_a == 4
        assert triangle.side_b == 6
        assert triangle.side_c == 5

    def test_triangle_create_with_type_error(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 'b', 3)

    def test_triangle_create_with_incorrect_sides(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 1, 2)

    def test_triangle_type_nonequilateral(self):
        assert Triangle(4, 6, 5).triangle_type() == 'nonequilateral'

    def test_triangle_type_equilateral(self):
        assert Triangle(4, 4, 4).triangle_type() == 'equilateral'

    def test_triangle_type_isosceles(self):
        assert Triangle(4, 5, 4).triangle_type() == 'isosceles'

    def test_triangle_perimeter(self):
        assert Triangle(4, 6, 5).perimeter() == 15