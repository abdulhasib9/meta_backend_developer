def calc_tax(bill,tax_rate):
    return (bill *tax_rate)/100.00

print("total tax: ",calc_tax(234,1.4))

#python scoop 
#global scope
my_global ="my global variable"

def local_test():
    #enclosed scope
    enclosed=4
    def innerfunc():
        localv =33
        print("enclosed",enclosed)
local_test()

#note the built in scoop is the python keyword like def and print etc...