list =[1,4,56,78,9]

print(*list)
print(list,sep=" ")
list.insert(len(list),5)

list.append("hero")

print(*list)

list.extend([323,565,676,4])

print(*list)

#removing the item 
list.pop(1)
print(*list)

del list[3]
print(*list)

#looping through the list 
for item in list:
    print(item)