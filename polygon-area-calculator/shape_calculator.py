class Rectangle:

    #construct the rectangle.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #show properties.
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    #change width.
    def set_width(self, new_width):
        self.width = new_width

    #change height.
    def set_height(self, new_height):
        self.height = new_height

    #calculate area.
    def get_area(self):
        return self.width * self.height

    #calculate perimeter.
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    #calculate diagonal.
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**0.5)

    #construct the shape with "*".
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = (self.width * "*" + "\n") * self.height
            return picture

    #calculate another shape to fit in.
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):

    #construct the square.
    def __init__(self, side):
        self.width = side
        self.height = side

    #show properties.
    def __str__(self):
        return f"Square(side={self.width})"

    #change side.
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side