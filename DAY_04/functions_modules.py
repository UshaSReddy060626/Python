#function 
def bake_cake(flavor="vanilla",layers=5):
    print(f"\nGathering ingredients for a {flavor} cake...")
    print(f" Mixing the batter and pouring into {layers} pans...")
    print(f"Baking in the oven at 350°F...")
    print(f" Cooling the layers and adding frosting...")
    return f"the {flavor} cake with {layers} layers is delicious"
my_cake=bake_cake()
print(my_cake)

# default arguments
def ice_cream(flavor="cookie and cream"):
    return flavor    
print(ice_cream())  #output:cookie and cream
print(ice_cream("strawberry"))  #output:strawberry

#keyword arguments
def buy_flowers(type,color):
    return f"These {color} {type} are beautiful "
print(buy_flowers(type="tulips",color="white"))

#args
def add(*num):
    return sum(num)
print(add(1, 2, 3, 4))

#kwargs
def info(**kwargs):
    print(kwargs)
info(name="Aarav",age=21,Branch="AIML")

#global variable
a=20
b=10
def add():
    print(a+b)
add()

#local variable
def multiply():
    m1=20
    m2=90
    print(m1*m2)
multiply()

#changing global
x="Hello"
def greet():
    global x
    x="HI"

greet()
print(x)

#lambda
def cube(x):
    return x*x*x
x=20
result=lambda x:x*x*x
print(result(x))


#import 
import math
print(math.sqrt(5))

#from import
from math import sqrt
print(sqrt(9))

#if __name__ == '__main__'
def even_or_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
if __name__ =="__main__":
    print(even_or_odd(30))


   