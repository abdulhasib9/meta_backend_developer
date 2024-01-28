prods = [
    ("prod1",30),
    ("prod2",40),
    ("prod4",4)
]


filterd =[x for x in prods if x[1]<30]
print(filterd)