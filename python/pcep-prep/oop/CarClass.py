class CarClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @classmethod
    def zero(cls):
        return CarClass(0,0)

# car = CarClass(23, 45)
#
# print(car.y)

car2 = CarClass.zero()
print(car2.x)