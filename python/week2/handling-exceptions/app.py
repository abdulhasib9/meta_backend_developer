def divide(a,b):
    return a/b

#print(divide(1,0))

try:
    print(divide(1,0))
except:
    print("something went wrong!")
    
#catching the actual message from the exception

try:
    print(divide(1,0))
except Exception as e:
    print(e,"can not divide by zero")
    #getting the actual error class
    print(e.__class__)
except Exception as e:
    print(e,"something went wrong!")