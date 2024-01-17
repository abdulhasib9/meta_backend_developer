bill_total =1245
discount1 =10 
discount2=20

if bill_total >100 and bill_total<200:
    print("Bille is greater than 100!")
    bill_total = bill_total -discount1
elif bill_total>200:
    print("the bill is more than 200")
    bill_total = bill_total-discount2
else:
    print("the bill is less than 100!")
    
print("Total bill is : "+str(bill_total))