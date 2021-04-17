from lesson3.figure import Triangle, Rectangle, Square, Circle, pi


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

    def test_add_area(self):
        # создаю инстанс прямоугольника чтобы получив его площадь, передать ее в add_area
        rect = Rectangle(5, 4)
        rect.get_area()
        # Triangle.area = 7.5, Rectangle.area = 20
        assert self.figure.add_area(rect) == 27.5
        assert self.figure.add_area('Not Figure instance') == TypeError


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

    def test_add_area(self):
        # создаю инстанс круга чтобы получив его площадь, передать ее в add_area
        circle = Circle(5)
        circle.get_area()
        # Circle.area = 78.53981633974483, Rectangle.area = 45
        assert self.figure.add_area(circle) == 123.53981633974483
        assert self.figure.add_area('Not Figure instance') == TypeError


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

    def test_add_area(self):
        # создаю инстанс треугольника чтобы получив его площадь, передать ее в add_area
        triangle = Triangle(3, 5)
        triangle.get_area()
        # Square.area = 9, Triangle.area = 7.5
        assert self.figure.add_area(triangle) == 16.5
        assert self.figure.add_area('Not Figure instance') == TypeError


class TestCircle:
    figure = Circle(4)

    def test_circle_area(self):
        assert self.figure.get_area() == 50.26548245743669

    def test_circle_perimeter(self):
        assert self.figure.get_perimeter() == 4 * pi * 2

    def test_get_figure_name(self):
        assert Circle.name == 'circle'

    def test_get_figure_angles(self):
        assert Circle.angles == 0

    def test_add_area(self):
        # создаю инстанс квадрата чтобы получив его площадь, передать ее в add_area
        square = Square(3)
        square.get_area()
        # Square.area = 9, Circle.area = 50.26548245743669
        assert self.figure.add_area(square) == square.area + self.figure.area
        assert self.figure.add_area('Not Figure instance') == TypeError
