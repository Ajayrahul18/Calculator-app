# swaping Two Numbers
'''x, y = 1, 2
print(f'x = {y}, y = {x}')
temp = x
x = y
y = temp
print(f'x = {x}, y = {y}')'''

# Arguments
'''def add(x, y, *args):
    total = x + y
    for i in args:
        total += i
    return total
print(add(10,20,30,40,50))'''

# **kwargs - accept a variable number of keyword \
# arguments as a dictionary

'''def information(**dict):
    print(dict)
infor = {'name' : 'Ajay',
'age' : 23,
'email' : 'xxx@gmail.com',
'password' : 'xxxx'}
information(**infor)
print(infor)'''

# Partial Multiply cation
# we dont have to create 2 fn
'''from functools import partial
def multiplay(x, y):
    return x*y
print(multiplay(10, 20))
x = 3
f = partial(multiplay, x)
print(f(10))'''

# Modules
# module is a separate Python source code file
# we can connect different module using 'import 'module name''

# The '__name__' variable allows you to check when the file is 
# executed directly or imported as a module.

# Stores system pages in this location
'''import sys
print(sys.prefix)'''

# When we use pip to install than this location
'''import site
print(site.getsitepackages())'''

# We cannot keep different versions of pip
# That why we use 'virtual environment'

# Virtual environment - each project will have its own directory
# modul'(venv)'

# f - strings
'''first_name = 'AJAY'
second_name = 'rahul'
print(f'Hello,{first_name}')
print(f'Hello,{second_name.upper()}')
print(f'Hello, {first_name.lower()} {second_name.upper()}')'''

# raw strings are help full when we want to add '\'
# '\' - escape = "r'comments"