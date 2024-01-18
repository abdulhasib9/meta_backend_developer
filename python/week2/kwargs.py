def sum(a,b):
    return a+b

print(sum(2,4))
#we can not add the third argument it will throw error 

#better version 
def sum2(*args):
    total=0
    for item in args:
        total+=item
    return total

print(sum2(32,4,5))

#kwargs 

def sum3(**kwargs):
    total =0
    for key,value in kwargs.items():
        total +=value
    return round(total,2)

print(sum3(coffee=2.44,cake=23,tea=32))
        
