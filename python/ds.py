list2 =[1,"name",1.55]

zeros = [0]*100
print(*zeros)

list_of_lists = [[12,34],[23,45]]

print(list_of_lists)

combined = list2+zeros
print(combined)

print("=====================================================================")
#generating numbers 0-19 in a list using list() funcution 
numbers = list(range(20))
print(numbers)

print("----------------------------------------------------------------")
#we can pass string object in list function because string is iterable 
chars = list("Hello World!")
print(chars)

print(len(zeros))

print("------------------------------------------------------------------")

#unpacking list
nums = [1,2,4]
num1,num2,num3 = nums

print(num1)
print(num2)
print(num3)

print("----------------------------------------------------------")

#unpacking specific items 
specific = list(range(20))
print(specific)
one,two, *others=specific
print(one)
print(two)
print(others)

print("************************************************************")
#iterating over the list 
new_list = list("Abdul hasib yousufzai")

for c in enumerate(new_list):
    #printing the index 
    print("index: "+str(c[0])+" values: "+c[1])
    
#we can also use unpacking list method to perform same job
for index,item in enumerate(new_list):
    print(index,item)
    
print("##############################################################")
#lambda demo 
# list_tuples =[
#     ("item1",20),
#     ("item2",10),
#     ("item3",4)
# ]

# list_tuples.sort(key=lambda items:list_tuples[1])
# print(list_tuples)

#adding new items 

list2=list(range(10))
list2.insert(5,200)
print(list2)
list2.append(400)
print(list2)
list2.pop()
print(list2)
list2.pop(5)
print(list2)

#removing unknown index item 
list3= list("hello world")
list3.remove("o")
print(list3)
for x in list3:
    if x =="o":
        list3.remove(x)
    print(x)
list3.clear()
print(list3)

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
list4 = list(range(5))
if 3 in list4:
    print(list4.index(3))
    
print(list4.count(3))

print("---------------------------------------------------------------")
list5 =[23,44,1,34,56,3,444,32]
#list5.sort(reverse=True)
print(list5)
print(sorted(list5, reverse=False))

#sorting lists with complex objects
list6=[
    ("prod1",34),
    ("prod2",4)

]
def item_sorted(item):
    return[1]
list6.sort(key=item_sorted,reverse=False)
print(list6)

list6.sort(key=lambda arguments : arguments[1])
print(list6)