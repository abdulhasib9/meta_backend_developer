items=[
    ("product1",30),
    ("product2",10),
    ("product3",40)
]

filterd_list = list(filter(lambda items:items[1]>10,items))
print(filterd_list)