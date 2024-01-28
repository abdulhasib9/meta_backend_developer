products = [
    ("product1",30),
    ("product2",40),
    ("product3",3)
]

filterd = list(filter(lambda item:item[1] <30,products))

print(filterd)

filterd_map = list(map(lambda item:item[1]<30,products))
print(filterd_map)

coffee_menu = [
    'Espresso',
    'Americano',
    'Latte',
    'Cappuccino',
    'Black Coffee',
    'Iced Latte',
    'Vanilla Latte',
    'Mocha',
    'Flat White',
    'Cold Brew',
    'Chai Latte',
    'Herbal Tea Latte',
    'Affogato',
    'Pumpkin Spice Latte',
    'Peppermint Mocha',
]

def filterd_coffee(coffee):
    if coffee[0]=="C":
        return coffee_menu 

filterd_fun = map(filterd_coffee,coffee_menu)

for x in filterd_fun:
    print(x)