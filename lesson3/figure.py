import math


class Figure:

    def error_func(self, name):
        print(f"Passed incorrect params for {self.name}")


class Triangle(Figure):
    name = 'triangle'
    angles = 3
    perimeter = 0
    area = 0

    def triangle_area(self, base, height):
        self.area = 0.5 * base * height
        if self.area > 0:
            print(f'{self.name} area is: {self.area}')
        else:
            self.error_func(self.name)

    def triangle_perimeter(self, a, b, c):
        self.perimeter = float(a + b + c)
        if a > 0 and b > 0 and c > 0:
            print(f'{self.name} perimeter is: {self.perimeter}')
        else:
            self.error_func(self.name)


class Rectangle(Figure):
    name = 'rectangle'
    angles = 4
    perimeter = 0
    area = 0

    def rectangle_area(self, a, b):
        self.area = float(a * b)
        if self.area:
            print(f"{self.name} area is: {self.area}")
        else:
            self.error_func(self.name)

    def rectangle_perimeter(self, a, b):
        if a and b:
            self.perimeter = float((a + b) * 2)
            print(f"{self.name} perimeter is: {self.perimeter}")
        else:
            self.error_func(self.name)


class Square(Figure):
    angles = 4
    name = 'square'
    __area = 0
    __perimeter = 0

    def square_area(self, a):
        if a:
            self.__area = a * a
            print(f"{self.name} area is: {self.__area}")
        else:
            self.error_func(self.name)

    def square_perimeter(self, a):
        if a:
            self.__perimeter = a * 4
            print(f"{self.name} perimeter is: {self.__perimeter}")
        else:
            self.error_func(self.name)


class Circle(Figure):
    """
    S = pi * r * r
    P = pi * r * 2
    """
    name = 'circle'
    angles = 0
    __area = 0
    __perimeter = 0

    def circle_area(self, r):
        if r:
            self.__area = math.pi * r * r
            print(f"{self.name} area is: {self.__area}")
        else:
            self.error_func(self.name)

    def circle_perimeter(self, r):
        if r:
            self.__perimeter = math.pi * r * 2
            print(f"{self.name} perimeter is: {self.__perimeter}")
        else:
            self.error_func(self.name)


first_figure = Triangle()
second_figure = Rectangle()
f3 = Square()
f4 = Circle()
f4.circle_perimeter(-5)