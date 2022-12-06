# "__str__" vs "__repr__" Magic Method
'''class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
    def __str__(self):
        return f'Hii, my name is {self.first_name} {self.second_name} and i am {self.age} years old'
    def __repr__(self):
        return f'Hii, my name is {self.first_name} {self.second_name} and i am {self.age} years old'
p = Person('Ajay', 'Rahul', 23)
print(p) #uses str() - Humaon readable
print(repr(p)) #uses repr() - Machine readable'''

# "__eq__"
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False
ajay = Person('Ajay', 23)
rahul = Person('Rahul', 23)
thiya = Person('Thiya', 20)

print(ajay == rahul) # her it call the __eq__ fn
print(ajay == thiya)
print(thiya == 20) # isinstance is used to show false'''

# "__bool__" - It returns true ro false
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __bool__(self):
        if self.age < 13 or self.age > 19:
            return False
        return True
if __name__ == '__main__':
    p = Person('Ajay', 23)
    print(bool(p))'''
# Getter and setter 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)# call setter method while initialize
    def set_age(self, age):
        if age < 0:
            raise ValueError('The age must be positive')
        self.age = age
    def get_age(self):
        return self.age
p = Person('Ajay', 23)
print(p.set_age(19))
