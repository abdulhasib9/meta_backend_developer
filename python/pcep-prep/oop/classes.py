class Point:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("drawing")


point1 = Point(32, 4)
print(type(point1))
print(isinstance(point1, Point))
print(point1)

point2 = Point(23, 44)
point2.x
