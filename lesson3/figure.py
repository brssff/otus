from math import pi as PI


class Figure:

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

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
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


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
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2


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
        return self.radius * self.radius * PI

    def get_perimeter(self):
        return PI * self.radius * 2
