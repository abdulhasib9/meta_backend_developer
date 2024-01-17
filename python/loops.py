for i in range(10):
    print(i)

favorites = ["cake","apple pie","chocolate"]

for item in favorites:
    print("i like : "+item)
    
    
#while loop

counter =0
while counter < len(favorites):
    print("i like this desert "+favorites[counter])
    counter +=1
    
#using loops with control flow statements 
favorites2 = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for item in favorites2: 
    if(item =="Churros"):
        # continue
        print("You love the perfect desert "+item)
        break
       
    else:
        print("desert "+item)