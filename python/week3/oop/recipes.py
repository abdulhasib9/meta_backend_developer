class Recipies:
    def __init__(self,dish,items,time) -> None:
        self.dish =dish
        self.items=items
        self.time=time
    
    def description(self):
        print(self.dish+" takes "+ str(self.items)+ \
              " to prepare in : "+ str(self.time))
        

pizza = Recipies("pizza",["cheeze","sauce","vegies"],45)
pasta = Recipies("pasta",["penny","sauce"],55)

print(pizza.items)
print(pasta.items)
print(pizza.description())
        