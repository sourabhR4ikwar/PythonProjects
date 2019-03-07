class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_values(self):
        print(self.x,self.y)


point1 = Point(10,11)
point1.print_values()
