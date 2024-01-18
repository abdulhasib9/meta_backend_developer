try:
    with open ("new.txt",'w') as file:
        file.writelines("this is my new file create by python")
except Exception as e:
    print(e,"File note exists")   
    
try:
    with open ("new2.txt",'a') as file:
        file.writelines("\nthis is my new file create by python")
except Exception as e:
    print(e,"File not exists") 