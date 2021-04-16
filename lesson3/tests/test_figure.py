import pytest
from lesson3.figure import Triangle, Rectangle, Square, Circle, PI


class TestTriangle:
    figure = Triangle(base=3, height=5, side_a=5, side_b=7, side_c=2)

    def test_triangle_area(self):
        assert self.figure.get_area() == 7.5

    def test_triangle_perimeter(self):
        assert self.figure.get_perimeter() == 14

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'triangle'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 3


class TestRectangle:
    figure = Rectangle(side_a=5, side_b=9)

    def test_rectangle_area(self):
        assert self.figure.get_area() == 45

    def test_rectangle_perimeter(self):
        assert self.figure.get_perimeter() == 28

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'rectangle'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 4


class TestSquare:
    figure = Square(side_a=3)

    def test_square_area(self):
        assert self.figure.get_area() == 9

    def test_square_perimeter(self):
        assert self.figure.get_perimeter() == 12

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'square'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 4


class TestCircle:
    @pytest.mark.parametrize("value, ex_result", [(3, PI * 3 * 3),(5, PI * 5 * 5)])
    def test_circle_area(self, value, ex_result):
        figure = Circle(value)
        assert figure.get_area() == ex_result

    @pytest.mark.parametrize("value, ex_result", [(3.5, 3.5 * PI * 2), (0, 0)])
    def test_circle_perimeter(self, value, ex_result):
        figure = Circle(value)
        assert figure.get_perimeter() == ex_result

    def test_get_figure_name(self):
        assert Circle.name == 'circle'

    def test_get_figure_angles(self):
        assert Circle.angles == 0
