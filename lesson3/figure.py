from math import pi


class Figure:

    name = None
    angles = None
    area = 0

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles


class Triangle(Figure):
    angles = 3
    name = 'triangle'

    def __init__(self, base, height, side_a=None, side_b=None, side_c=None):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        self.area = 0.5 * self.base * self.height
        return self.area

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError


class Rectangle(Figure):
    name = 'rectangle'
    angles = 4

    def __init__(self, side_a, side_b=None):
        # если передана только одна сторона, то это квадрат, иначе - прямоугольник
        if not side_b:
            self.side_a = side_a
            self.side_b = side_a
        else:
            self.side_a = side_a
            self.side_b = side_b

    def get_area(self):
        self.area = self.side_a * self.side_b
        return self.area

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError


class Square(Rectangle):
    name = 'square'


class Circle(Figure):
    """S = pi * r * r
       P = pi * r * 2"""
    name = 'circle'
    angles = 0

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        self.area = self.radius * self.radius * pi
        return self.area

    def get_perimeter(self):
        return pi * self.radius * 2

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError
