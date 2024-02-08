try:
    age = int(input("please enter your age:"))

except ValueError as err:
    print("invalid value for age ")
    print(err.__cause__)
else:
    print("No exception raised")
print("code running continues")

def calculate (age):
    if age<=0:
        raise ValueError ("age cannot be zero")
    return 10/age
calculate(0)