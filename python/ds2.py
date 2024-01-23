items =[
    ("item1",23),
    ("item2",4),
    ("item3",55)
]

prices = []

for x in items:
    prices.append(x[1])
print(prices)

s = map(lambda item:item[1],items )
print(s)
for x in s:
    print(x)
    
ss=list(map(lambda item:item[1],items))
print(ss)

sss = list(map(lambda item:item[1]>5,items))
print(sss)