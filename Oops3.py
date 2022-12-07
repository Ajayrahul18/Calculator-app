# property
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def age(self):
        return self._age
    age = property(fget=age)
p = Person('Ajay', 23)
print(p.age)'''

# @property
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
           if value.strip() == '':
            raise ValueError('Name cannot be empty')
           self._name = value
    age = age.setter(age)
ajay = Person('Ajay', 23)
print(ajay.age)'''

# Readonly Memory
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property #area is a property of Circle
    def area(self):
        return math.pi*self.radius**2
c = Circle(10)
print(c.area())