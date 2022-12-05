#creating a class 
'''class Clac:
    def add(self):
        print(x + y)
    def sub(self):
        print(x - y)
    def mul(self):
        print(x * y)
    def div(self):
        print(x / y)
x = int(input("Enter the 1st number: "))
y = int(input("Enter the 2st number: "))
#creating object for class
c = Clac()
choise = 1
while(choise != 0):
    print("1. Add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    choise = int(input("Enter your choise: "))
    if choise == 1:
        #calling function
        c.add()
    elif choise == 2:
        c.sub()
    elif choise == 3:
        c.mul()
    elif choise == 4:
        c.div()
    else:
        print("Invalid choise")'''

'''def rec(x):
    if x > 0:
       print(x)
       rec(x-1)
rec(5)'''

'''def sum(x):
    if x != 0:
        return(x + sum(x-1))
    return(0)
print(sum(5))'''

skills = {'Drawing', 'Swimming', 'Singing'}
print(set(map(lambda skill: skill.upper(), skills)))

