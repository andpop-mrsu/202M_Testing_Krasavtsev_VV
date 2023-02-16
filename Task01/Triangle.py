from triangle_func import IncorrectTriangleSides


class Triangle:
    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_c, int):
            raise IncorrectTriangleSides('Incorrect triangle sides: Invalid data type')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise IncorrectTriangleSides('Incorrect triangle sides: Triangle does not exist')

    def triangle_type(self) -> str:
        if self.side_a and self.side_a != self.side_c and self.side_b != self.side_c:
            return "nonequilateral"
        elif self.side_a == self.side_b == self.side_c:
            return "equilateral"
        else:
            return "isosceles"

    def perimeter(self) -> int:
        return self.side_a + self.side_b + self.side_c