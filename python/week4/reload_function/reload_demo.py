import test
import importlib
import os 

importlib.reload(test)
importlib.reload(test)
importlib.reload(test)

contents = os.listdir(r'/Users/thebeast/Documents/meta_backend_developer/python/week4/reload_function/')

print(contents)
class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())