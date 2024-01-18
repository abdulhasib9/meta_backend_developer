set_a = {1,2,4,5,6}
set_a.add(45)
print(set_a)
set_a = set_a.discard(2)
print(set_a)

#we can not access set element by index

a={1,2,4,5,6}
b={6,3,5,23}

print(a.union(b))
#another way
print(a | b)

#getting the matched items in two sets 
print(a.intersection(b))

#getting the unique items which is not in set b
print(a.difference(b))

#print all the elements that are represeted in boot sets 

print(a.symmetric_difference(b))
print(a^b)