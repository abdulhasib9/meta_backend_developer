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
    