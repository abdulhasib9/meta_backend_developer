file = open("C:\\Users\\thebeast\Desktop\\meta_backend_developer\\python\\week2\\handling-exceptions\\test.txt", mode = 'r')
data = file.readline()
print(data) 
file.close()

#another way to open the file note:this will close the file for you
with open("C:\\Users\\thebeast\Desktop\\meta_backend_developer\\python\\week2\\handling-exceptions\\test.txt",mode="r") as file2:
    data2=file2.readline()
print(data2)

    