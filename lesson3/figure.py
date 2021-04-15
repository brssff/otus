PI = 3.14
# сознательно не хочу импортить math ради 'pi'


class Figure:
    area = 0

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles


class Triangle(Figure):
    angles = 3
    name = 'triangle'
    perimeter = 0
    area = 0

    def __init__(self, name, angles):
        if self.name == name and self.angles == angles:
            super().__init__(name, angles)
        else:
            raise NameError(f'Passed params: {name} {angles}, expected: {self.name} {self.angles}')

    def get_area(self, base, height):
        self.area = 0.5 * base * height
        return self.area

    def get_perimeter(self, a, b, c):
        self.perimeter = a + b + c
        return self.perimeter

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles


class Rectangle(Figure):
    name = 'rectangle'
    angles = 4
    perimeter = 0
    area = 0

    def __init__(self, name, angles):
        if self.name == name and self.angles == angles:
            super().__init__(name, angles)
        else:
            raise NameError(f'Passed params: {name} {angles}, expected: {self.name} {self.angles}')

    def get_area(self, a, b):
        self.area = a * b
        return self.area

    def get_perimeter(self, a, b):
        self.perimeter = (a + b) * 2
        return self.perimeter

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles


class Square(Figure):
    angles = 4
    name = 'square'
    area = 0
    perimeter = 0

    def __init__(self, name, angles):
        if self.name == name and self.angles == angles:
            super().__init__(name, angles)
        else:
            raise NameError(f'Passed params: {name} {angles}, expected: {self.name} {self.angles}')

    def get_area(self, a):
        self.area = a * a
        return self.area

    def get_perimeter(self, a):
        self.perimeter = a * 4
        return self.perimeter

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles


class Circle(Figure):
    """S = pi * r * r
       P = pi * r * 2"""
    name = 'circle'
    angles = 0
    area = 0
    perimeter = 0

    def __init__(self, name, angles):
        if self.name == name and self.angles == angles:
            super().__init__(name, angles)
        else:
            raise NameError(f'Passed params: {name} {angles}, expected: {self.name} {self.angles}')

    def get_area(self, r):
        self.area = PI * r * r
        return self.area

    def get_perimeter(self, r):
        self.perimeter = PI * r * 2
        return self.perimeter

    def get_angles(self):
        return self.angles

    def get_name(self):
        return self.name

# метод add_area(figure) который должен принимать другую
# геометрическую фигуру и возвращать сумму площадей этих фигур.