import pytest
from lesson3.figure import *


class TestTriangle:
    figure = Triangle('triangle', 3)

    @pytest.mark.parametrize("base, height, ex_result", [(5, 3, 7.5), (10, 99, 495.0), (0, 7, False)])
    def test_triangle_area(self, base, height, ex_result):
        assert self.figure.get_area(base, height) == ex_result

    @pytest.mark.parametrize("a, b, c", [(5, 7, 2), (0.5, 0.99, 2)])
    def test_triangle_perimeter(self, a, b, c):
        assert self.figure.get_perimeter(a, b, c) == a + b + c

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'triangle'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 3


class TestRectangle:
    figure = Rectangle('rectangle', 4)

    def test_rectangle_area(self):
        assert self.figure.get_area(3, 1.5) == 4.5

    def test_rectangle_perimeter(self):
        assert self.figure.get_perimeter(3, 2) == 10

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'rectangle'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 4


class TestSquare:
    figure = Square('square', 4)

    def test_square_area(self):
        assert self.figure.get_area(5) == 25

    def test_square_perimeter(self):
        assert self.figure.get_perimeter(0.5) == 2

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'square'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 4


class TestCircle:
    figure = Circle('circle', 0)

    def test_circle_area(self):
        assert self.figure.get_area(3) == PI * 3 * 3

    @pytest.mark.parametrize("r, expected", [(3.5, 3.5 * PI * 2), (0, 0)])
    def test_circle_perimeter(self, r, expected):
        assert self.figure.get_perimeter(r) == expected

    def test_get_figure_name(self):
        assert self.figure.get_name() == 'circle'

    def test_get_figure_angles(self):
        assert self.figure.get_angles() == 0
