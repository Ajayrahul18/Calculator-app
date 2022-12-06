# Creating class attribute
'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f'Hii, I am {self.name}'
    def ages(self):
        return f'I am {self.age}'
#per = Person('Ajay', 23)
#print(per.greet())
#print(per.ages())'''
# class method - A class method is shared by all instances
'''@classmethod
    def create_anon(cls):
        return Person('Rahul', 32)
anon = Person.create_anon()
print(anon.name)
print(anon.age)'''

# Static Method - It is not bound to class
# it is used to group logically related function
'''class TempConvtr:
    @staticmethod
    def Cel_to_fah(c):
        return 9 * c / 5 + 32
    @staticmethod
    def fah_to_cel(f):
        return 5 * (f - 32) / 9
c = TempConvtr.Cel_to_fah(30)
print(c)
f = TempConvtr.fah_to_cel(86)
print(f)'''

# inheritance
'''class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    def work(self):
        return f'I am a {emp.job_title} in this company'
emp = Employee('Ajay', 23, 'Intern')
print(emp.greet())
print(emp.ages())
print(emp.work())'''

# An object is a container that contains the state and mrthods.
# Python stores class variables in the __dict__ attribute

# Encapsulaton
# Private attribute - Connot accessible from out side
# Create name with '_' then treate it as private class
'''class Counter:
    def __init__(self):
        self._current = 0
    def increment(self):
        self._current += 1
    def value(self):
        return self._current
    def reset(self):
        self._current = 0
cou = Counter()
cou.increment()
cou.increment()
cou.increment()
#cou._current = 99 it can stilll change
print(cou.value())'''

# Working of class attributes
'''class Test:
    x = 10
    def __init__(self):
        pass#self.x = 20
test = Test()
print(test.x)
print(Test.x)'''

# static method 
class TempConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5*(f+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TempConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TempConverter.CELSIUS:
            symbol = '°C'
        elif unit == TempConverter.KEVIN:
            symbol = '°K'

        return f'{value}{symbol}'
f = TempConverter(35)
print(TempConverter.format(f,TempConverter.FAHRENHEIT))