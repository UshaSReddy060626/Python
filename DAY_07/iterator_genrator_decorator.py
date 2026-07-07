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


   