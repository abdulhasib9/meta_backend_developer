import random

with open ("new.txt",'r') as file:
    print(file.read())
    print(file.readline())
    
f = open("new.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))
f.close()