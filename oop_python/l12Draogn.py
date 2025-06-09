class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2:
            return True
        else:
            return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        x1 = x - self.__fire_range
        y1 = y - self.__fire_range
        x2 = x + self.__fire_range
        y2 = y + self.__fire_range

        hit_units = []
        for unit in units:
            if unit.in_area(x1, y1, x2, y2):
                hit_units.append(unit)

        return hit_units
