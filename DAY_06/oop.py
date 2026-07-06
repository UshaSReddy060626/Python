#object
class car():
    pass
car1=car()
car2=car()

#init()
class chair:
    def __init__(self,color,material):
        self.color=color
        self.material=material
    def describe(self):
        return f"my chair is made of {self.material} and its in color {self.color}"
my_new_chair=chair("brown","wood")
print(my_new_chair.describe())

#self
class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def describe(self):
        return f"i am {self.fname} and i am {self.lname}"
my_new_Name=student("rahul","sonia")
print(my_new_Name.describe())

#instance
class student:
    def __init__(self,branch,college):
        self.branch=branch
        self.college=college
    def describe(self):
        return f"i am pursuing {self.branch} at {self.college}"
my_student=student("AIML","SSIT")
print(my_student.branch)
print(my_student.college)
print(my_student.describe())

#class attribute
class phone:
    has_touchscreen=True
    def __init__(self,color):
        self.one_color=color
        self.second_color=color
phone_one=phone("orange")
phone_two=phone("black")
print(phone_one.has_touchscreen)
print(phone_two.has_touchscreen)
print(phone_one.one_color)
print(phone_two.second_color)

#inheritance
#single inheritance
class animal:
    def eat(Self):
        return "eating food......."
class dog(animal):
    def bark(self):
        return "woof!!!"

my_dog=dog()
print(my_dog.bark())
print(my_dog.eat())

#multiple inheritance
class teacher:
    def teach(self):
        return ("teaching")
class student:
    def study(self):
        return ("studying")
class assistant(teacher,student):
        pass
my_Assistant=assistant()
print(my_Assistant.teach())
print(my_Assistant.study())

#multi-level inheritance
class grandparent:
    def jewellery(self):
        return "vintage piece"
class parents(grandparent):
    def house(self):
        return "a family home"
class child(parents):
    def car(self):
        return "my new car"
my=child()
print(my.jewellery())
print(my.house())
print(my.car())

#polymorphism
class dog:
    def sound(self):
        return "bark..."
class cat:
    def sound(self):
        return "meow..."
animal=[dog(),cat()]
for a in animal: 
    print(a.sound())

#encapsulation
#public
class dog:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return "bark..."
class cat:
    def __init__(self,name):
        self.name=name
    def sound(self):
        return "meow..."
animal=[dog("cookie"),cat("peachy")]
for a in animal: 
    print(f"{a.name} {a.sound()}")
    

#protected
class dog:
    def __init__(self,name_of):
        self._name_of=name_of
    def sound(self):
        return "bark..."
class cat:
    def __init__(self,name_of):
        self._name_of=name_of
    def sound(self):
        return "meow..."
animal=[dog("cookie"),cat("peachy")]
for a in animal: 
    print(f"{a._name_of} {a.sound()}")
    

#private
class dog:
    def __init__(self,name_of):
        self.__name_of=name_of
    def get_private_name(self):
        return self.__name_of  
    def sound(self):
        return "bark..."
class cat:
    def __init__(self,name_of):
        self.__name_of=name_of
    def get_private_name(self):
        return self.__name_of  
    def sound(self):
        return "meow..."
animal=[dog("cookie"),cat("peachy")]
for a in animal: 
    print(f"{a.get_private_name()} {a.sound()}")

#property
class student:
    def __init__(self):
        self._age=18
    @property
    def age(Self):
        return self._age