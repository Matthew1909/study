# @property
# Used to make getter, setter and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter:
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Setter:
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("The new value must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("The new value must be greater than zero")

    # Deleter:
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")


rectangle = Rectangle(3, 4)

rectangle.width = 20
rectangle.height = 10

# print(rectangle.width)
# print(rectangle.height)

del rectangle.width
del rectangle.height
