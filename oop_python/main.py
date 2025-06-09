class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        pass

    def get_right_x(self):
        pass

    def get_top_y(self):
        pass

    def get_bottom_y(self):
        pass

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
