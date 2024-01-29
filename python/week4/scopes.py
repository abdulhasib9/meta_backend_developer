
def d():
    animal ="dog"
    def c():
        nonlocal animal
        animal ="cat"
    print("before calling c function "+animal)
    c()
    print("after calling c function "+animal)

animal = "girafe"

print("global animal "+ animal)
d()