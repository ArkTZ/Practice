class Point():
    def set_coordinates(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def get_distance(self, value):
        if isinstance(value, Point):
            return ((self.x -value.x)  ** 2 +(self.y -value.y)**2)**0.5
        else:
            print("Передана не точка")