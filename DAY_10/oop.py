#property
class Student:
    def __init__(self):
        self._marks = 90
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self._marks = value
        else:
            print("Invalid Marks!")
s = Student()
print(s.marks)
s.marks = 95
print(s.marks)
s.marks = 500

#classmethod
class student:
    college="ssit"
    @classmethod
    def show_college(cls):
        print(cls.college)
student.show_college()

#static
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
print(Calculator.add(5,3))

#__str__
class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Student Name : {self.name}"
s=Student("Usha")
print(s)

# __len__
class Basket:
    def __init__(self):
        self.items=["Apple","Mango","Orange"]
    def __len__(self):
        return len(self.items)
b=Basket()
print(len(b))

#__getitem__
class Basket:
    def __init__(self):
        self.items=["Apple","Banana","Mango"]
    def __getitem__(self,index):
        return self.items[index]
b=Basket()
print(b[0])

#__setitem__
class Basket:
    def __init__(self):
        self.items=["Apple","Banana"]
    def __setitem__(self,index,value):
        self.items[index]=value
b=Basket()
b[0]="Grapes"
print(b.items)

#__call__
class hi:
    def __call__(self):
        print("python is fun")
r=hi()
r()


#abstract base class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
class Bike(Vehicle):
    def start(self):
        print("Bike Started")
c=Car()
c.start()
b=Bike()
b.start()