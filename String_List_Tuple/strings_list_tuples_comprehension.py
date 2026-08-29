#strings
fruit = " orange ,apple"
#string methods
print(len(fruit))
print(fruit[0])
print(fruit.upper())
print(fruit.lower())
print(fruit.replace("e", "u"))
print(fruit.startswith("o"))
print(fruit.split(","))
print(fruit.strip())
#slicing
num=[10,20,30,40,50,60,70]
print(num[0:len(num)])#full slicing
print(num[0:7])#range slicing
print(num[::-1])#reversing a string
print(num[-3:-1])#negative slicing
print(num[-5:-1:2])#step slicing
print(num[:3])#partial slicing

#lists
basket=["books","pens",10,"cards"]
name=["aarav","samaira"]
#methods
print(basket[0:3])
print(basket[::-1])
basket.append("chocolates")
print(basket)
print(basket.count("books"))
print(basket.pop(0))#with index
print(basket.pop())#without index
print(basket)
basket.insert(0,45)
print(basket)
basket.extend(name)
print(basket)
name.sort(reverse=True)
print(name)

#tuples
numbers=(1,2,3,4,5,6,7,1,2,3,4)
print(numbers.count(1))
print(numbers.index(1,0,5))
print(numbers[-5])

#tuple unpacking
objects=["🔦","💡"]
item1,item2=objects
print(item1)
print(item2)

#list comprehension
animals=["dog","cat","koala"]
result=[a +"⭐" for a in animals]
print(result)
 #list comprehension
nums=[1,2,3,4,5,6,7]
result=[n*2 for n in nums]
print(result)
#list comprehension
word=["hello","world"]
result=[w.upper() for w in word]
print(result)
#set comprehension
words = ["Apple", "apple", "APPLE", "Banana", "banana"]
result={w.lower() for w in words}
print(result)
#set comprehesnion
stickers=["⭐","🔊","😊","😁","😊","😁","⭐","⭐"]
result={s for s in stickers}
print(result)
#set comprehension
prices = [10, 20, 10, 40, 20]
result={p/2 for p in prices }
print(result)
#dictinary comprehension
toys = ["🧸", "🚗", "🎨"]
result={t:"$0" for t in toys}
print(result)
#dictinary comprehension
words = ["cat", "apple", "banana"]
result={w:len(words) for w in words}
print(result)
#dictinary comprehension
numbers = [1, 2, 3]
result={n:n*2 for n in numbers}
print(result)
