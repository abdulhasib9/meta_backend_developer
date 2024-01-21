list = [1,2,3]

def add_item(item):
    list.append(item)
    return list

#making the above function a pure function
def add_item_pure(lst,item):
    nl=lst.copy()
    nl.append(item)
    return nl 
print(add_item(4))

new_list =(add_item_pure(list,5))
print(new_list)
