class Clac:
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
c = Clac()
choise = 1
while(choise != 0):
    print("1. Add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    choise = int(input("Enter your choise: "))
    if choise == 1:
        c.add()
    elif choise == 2:
        c.sub()
    elif choise == 3:
        c.mul()
    elif choise == 4:
        c.div()
    else:
        print("Invalid choise")
