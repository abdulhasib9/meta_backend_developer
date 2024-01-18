sample_dic = {1:"coffe",2:"tea",3:"water",'juice':"mango"}
sample_dic[2]="mint Tea"
#dictional wont allow duplicate values
print(sample_dic)
print(sample_dic["juice"])
sample_dic['new']="fruits"

print(sample_dic)

#delete an item from dictionary 
del sample_dic[1]
print(sample_dic)


#iterating through dictionary 
for key,value in sample_dic.items():
    print(str(key)+": "+value)
    
