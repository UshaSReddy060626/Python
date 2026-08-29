#async and await
import asyncio
async def hello():
    print("start")
    await asyncio.sleep(2)
    print("end")
asyncio.run(hello())

#asyncio
import asyncio
async def task():
    print("hi")
asyncio.run(task())

#asyncio.gather()
import asyncio
async def one():
    print("task 1")
async def two():
    print("task 2")
async def main():
    await asyncio.gather(one(),two())
asyncio.run(main())

#threading
import threading
def work():
    print("running")
t=threading.Thread(target=work)
t.start()

#thread class and target
import threading
def greet():
    print("hello")
t=threading.Thread(target=greet)
t.start()

#global interpreter lock
import threading
def work():
    for i in range(3):
        print(i)
threading.Thread(target=work).start()
threading.Thread(target=work).start()

# multiprocessing module
import multiprocessing
def work():
    print("Working")
if __name__ == "__main__":
    p = multiprocessing.Process(target=work)
    p.start()
    p.join()

# process and pool classes
from multiprocessing import Process
def hello():
    print("Hello")
if __name__ == "__main__":
    p = Process(target=hello)
    p.start()

#pool
from multiprocessing import Pool
def square(x):
    return x*x
if __name__ == "__main__":
    with Pool(2) as p:
        print(p.map(square,[1,2,3]))

#memory: generator vs list
numbers=(x for x in range(5))
print(next(numbers))
print(next(numbers))

#comprehension efficiency

#without comprehension
num=[]
for i in range(5):
    num.append(i)
print(num)

#with comprehension
num=[i for i in range(5)]
print(num)

#unittest module
import unittest
class test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+3,5)
unittest.main()

#pytest
def test_add():
    assert 2+3==5