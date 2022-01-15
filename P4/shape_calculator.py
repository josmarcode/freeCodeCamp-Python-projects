class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, n):
        self.width = n

    def set_height(self, n):
        self.height = n

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pic = ''
        for i in range(self.height):
            pic += f'{"*" * self.width}\n'

        return pic

    def get_amount_inside(self, figure):
        return self.get_area() // figure.get_area()


class Square(Rectangle):
    def __init__(self, s):
        self.height = self.width = s

    def __str__(self):
        return f'Square(side={self.height})'

    def set_side(self, n):
        self.height = self.width = n

    def set_width(self, n):
        self.set_side(n)

    def set_height(self, n):
        self.set_side(n)
