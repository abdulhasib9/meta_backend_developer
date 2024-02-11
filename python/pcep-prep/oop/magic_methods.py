# class Point:
#     def __init__(self,x,y) -> None:
#         self.__pri ="private"
#         self.x=x
#         self.y=y
        
#     def __eq__(self, other) -> bool:
#         return self.x ==other.x and self.y == other.y
#     def print_private(self):
#         print(self.__pri)
    

# point = Point(23,4)
# other = Point(23,4)

# print(point == other)
# print(point.print_private())

# class Products:
#     def __init__(self, price) -> None:
#         self.set_price(price)
        
#     def get_price(self):
#         return self.__price
#     def set_price(self,value):
#         if value <0:
#             raise ValueError("Value can not be less than zero")
#         else:
#             self.__price = value

# product = Products(50)
# print(product.get_price())
# print(product.set_price(-50))

class Products:
    def __init__(self, price) -> None:
        self.price = price
    @property   
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if value <0:
            raise ValueError("Value can not be less than zero")
        else:
            self.__price = value

product = Products(30)
print(product.price)
product.price = 49
print(product.price)