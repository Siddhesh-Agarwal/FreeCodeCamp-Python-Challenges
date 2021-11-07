class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * (self.height)

    def get_amount_inside(self, shape):
        if type(shape) == Square:
            return (self.width // shape.side) * (self.height // shape.side)
        elif type(shape) == Rectangle:
            return max((self.width // shape.width) * (self.height // shape.height), (self.width // shape.height) * (self.height // shape.width))

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def get_amount_inside(self, shape):
        if type(shape) == Square:
            return (self.side // shape.side) ** 2
        elif type(shape) == Rectangle:
            return (self.side // shape.width) * (self.side // shape.height)