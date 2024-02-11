class Animal:
    def __init__(self) -> None:
        print("Animal Constructor Called!")
        self.age =1
        
    def eat(self):
        print("eat")
        
class Mamal(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.weight =23
        print("mamal constructor called!")
        
m = Mamal()
print(m.age)
print(m.weight)