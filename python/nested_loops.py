import time
starta_time = time.time()
#outer loop 
for i in range(100):
    #inner loop 
    for j in range(100):
        print(0,end =" ")
    print()
    
print(round(time.time()-starta_time,2))