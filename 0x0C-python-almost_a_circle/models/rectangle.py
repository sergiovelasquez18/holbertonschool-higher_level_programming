#!/usr/bin/python3
"""the module creates the class that inherits from Base"""


from models.base import Base # type: ignore


class Rectangle(Base):
    """A class named Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangule class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """print in stdout the Rectangle instance with the character #"""
        for rows in range(self.__y):
            print()
        for rows in range(self.__height):
            for cols in range(self.__x):
                print(" ", end="")
            for cols in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return the informal representation of the object"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
        self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args):
        """Updates atributtes"""
