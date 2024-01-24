class Myclass: 
    # pass 
    print("hello")

myclass= Myclass()

bravo = 3
# b = B() we can not initiate the object befor class declaration this will throw an error
class B:
    bravo = 5
    print("Inside class B")
c = B()
# print(b.bravo)