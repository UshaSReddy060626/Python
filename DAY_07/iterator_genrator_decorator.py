#iter
fruits=["apple","strawberry","orange"]
a=iter(fruits)
print(next(a))
print(next(a))
print(next(a))

"""iter() → makes an iterator

next() → gives one item

__next__() → same as next()"""

#custom iter
class numbers:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=5:
            value=self.num
            self.num+=1
        return value
        raise StopIteration

n=numbers()
for i in n:
    print(i)

#yeild
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
n=numbers()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))

#generator
def count():
    for i in range(5):
        yield i
for i in count():
        print(i)

#generator expression
square=(x*x for x in range(7))
print(square)
for i in square:
    print(i)

#decorator
def wrap(func):
     def inside():
          print("start")
          func()
          print("end")
     return inside
@wrap
def hi():
    print("python is fun.")  
hi()

#class decorator
def price(cls):
     cls.price=10
     return cls
@price
class toy:
     pass
print(toy.price)

#map
def double(x):
     return x*2
marks=[85,90,95]
result=map(double,marks)
print(list(result))

#filter
def even(x):
     return x%2==0
num=[1,3,5,7,8,2,6]
result=filter(even,num)
print(list(result))

#reduce
from functools import reduce
def add(a,b):
     return a+b
numbers=[1,4,8,7,9]
result=reduce(add,numbers)
print(result)




   