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

def filter_coffee(coffee):
    if coffee[0]=='C':
        return coffee

#filtering data using map function
map_coffee = map(filter_coffee,coffee_menu)
print(map_coffee)
for i in map_coffee:
    print(i)

#filtering same data with filter function 
filtered_coffee = filter(filter_coffee,coffee_menu)
print(filtered_coffee)
for x in filtered_coffee:
    print(x)

#map function will return all records and put None for un matched items
#filter function will return all record but will return a new list with only matching items