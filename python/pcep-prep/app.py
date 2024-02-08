# multi_line = """
# this is python variable with multiple lines 
# """
# print(multi_line)

# print(list(multi_line))
# x,y=1,3

# print(y,x)


# age: int =20    
# print( id (age))
# age = "name"
# print ( id(age))
# print(age)

# x=[1,2,4]
# print(id(x))

# x.append(5)
# print(id(x))

# string= "python programming"
# print(string[-2])

# print(string[0:3])

# print(id(string))

# string += " another"

# print(string)

# print(id(string))

# print(id(string[1]))

# first = "abdul hasib"
# last = "yousufzai"

# full_name = f"{first} {last}"

# print(full_name)

# print(full_name.upper())
# print(full_name.lower())
# print(full_name.rstrip())
# print(full_name.title())
# print(full_name.find("h"))
# print(full_name.replace("a","_"))

# print("hasib" in full_name)
# print("hasib" not in full_name)


# x = 0b101

# print(x)

# print(hex(x))

# x=10+3
# x=10-3
# x=10//3
# print(x)
# x=10/3
# print(type(x),x)
# print(10**3)

# x = input("x: ")
#
# print(bool(x))

# age = 2
# if age >=20 and age<60:
#     print("you are eligible!")
# else:
#     print("you are not eligible")

# age=23
# message = "eligible" if age >18 else "not eligible"
# print(message)

# for x in range(0,10,2):
#     print(x)

# names = ["jason",'hasob']
# for x in names:
#     if x.startswith("jj"):
#         print("Found")
#         break
# else:
#     print("Not Found!")


# guess = 0
# answer =5
# while guess != answer:
#     guess = int(input("Please guess the number!"))
#
# else:
#     print(f"Congratulations you guessed it it is number {guess} ")
# def sum (num:int,num2:int=1)->int:
#     return "string"
# print(sum(3))


# def multiply (*list):
#     number =1
#     for x in list:
#         number *=x
#     return number
#

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# print(multiply(2,2,2))

# user_input = int(input("please enter a number "))
# if user_input %3 ==0 and user_input %5==0:
#     print("FizzBuzz")
# elif user_input %3 ==0:
#     print("Fizz")
# elif user_input %5==0:
#     print("Buzz")
# else:
#     print(user_input)

# list_num = list(range(20))
# print(list_num)
# print(list_num[::-1])
#
# first,second, *others=list_num
# print(first)
# print(others)


# letters = ["a","b","c"]
# for key,values in enumerate(letters):
#     print(key, values)
#
# letters.append("d")
# print(letters)
# letters.insert(0,"zero")
# print(letters)
# letters.pop()
# print(letters)
# letters.remove("b")
# del letters[0:2]
# print(letters)
# letters.clear()
# print(letters)

# print(letters.count("a"))
# if "d" in letters:
#     print(letters.index("d"))
# print(len(letters))

#list_numbers=[2,44,12,33,445,123]

# list_numbers.sort()
# print(list_numbers)
# list_numbers.sort(reverse=True)
# print(list_numbers)

# print(sorted(list_numbers,reverse=True))
# print(list_numbers)

# items =[
#     ("product1",14),
#     ("product2",10),
#     ("product3",4)
# ]
# def sort_items(item):
#     return item[1]
# items.sort(key=sort_items)
# print(items)

#using the lambda expression
# items.sort(key=lambda item:item[1])
# print(items)

# price_list = list(map(lambda item:item[1],items))
# print(price_list)
# expensive = list(filter(lambda item:item[1]>=10,items))
# print(expensive)

#list comprehension
# prices = [item[1] for item in items]
# print(prices)
#
# expensive =[item[1]>=10 for item in items]
# print(expensive)
# expensive2 = [item for item in items if item[1]>=10]
# print(expensive2[0:3])

# list1 =[12,3,5]
# list2=[2,34,5]
#
# print(list(zip("abc",list1,list2)))

# items =[
#     ("prod1",39),
#     ("prod2",9),
#     ('prod3',23)
#
# ]
#
# sorted_prices = [item[1] for item in items if item[1]>9]
# print(sorted_prices)
#ques in python

# from collections import deque
# deque_list = deque([])
# deque_list.append(1)
# deque_list.append(2)
# deque_list.append(3)
# deque_list.popleft()
# print(deque_list)
# if not deque_list:
#     print("deque list is empty")

#touples
# first = 1,2
# print(type(first))
# second = (1,2,4,5)
# if 10 in second:
#     print("10 is available in list")
# else:
#     print("sorry 10 is not available")
#
# stringtouple= tuple("programming")
# print(stringtouple)
# f,s,t,*d=stringtouple
# print(f)
# print(d)

#swapping numbers
# x=10
# y=11
# x,y=y,x
# print(x)
# print(y)

# from array import array
# array_demo = array('i',[12,334,55,3])
# array_demo.append(32)
# print(array_demo)

# dic = dict(y=23,x=2,z=3)
# print(dic)
#
# for x,y in dic.items():
#     print(x,y)
#
#
#
# del dic["x"]
# print(dic)

# values = [x *2 for x in range(5)]
# print(values)

# dic = {x: x*2 for x in range(5)}
# print(dic)

#generator objec
# values = (x*2 for x in range(1,100000))
# from sys import getsizeof
# print(getsizeof(values))
# values =[x*2 for x in range(100000)]
# print(getsizeof(values))

#unpacking values
# values = [*"Hello"]
# print(*values)
#
# dic = {'x':29}
# dic2={'x':34,'y':23}
#
# dic3 = {**dic,'x':"hello",**dic2}
# print(dic3)

