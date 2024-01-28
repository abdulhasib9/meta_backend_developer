list1=[12,3,4]
list2=[223,5,6,45]

print(list(zip("abc",list1,list2)))

zip_list = list(zip("abc",list1,list2))

first = zip_list[0]

print(first)

print(first[1])

print("---------------------------------- Dictionaries -----------------------------------------")

dic = {
    "x":"name",
    "y":"last_name"
}

print(dic["x"])

for x,y in dic.items():
    print(y)

#using comprehension to create dictionaries
    
    
new_dic = {x: x * 2 for x in range(4)}

print(new_dic)

