#set
a={1,2,3,4,5,6,7,9,0}
b={2,4,6,8,9,0,1,7}
# creating set 
# method 1
set1={2,3,4}
#method 2
set2=([4,67,8])


#empty set
fruits={} # creats dictinary
print(type(fruits))
#correct method
fruits=set()
print(type(fruits))

#adding elements
a.add(8)
print(a)
#removing elements
a.remove(9)
print(a)
"""remove deletes elements from a set and throws error(key_error) if the element is missing and 
discard also removes elements but it does not throw any error"""
#discard elements
a.discard(0)
print(a)
#pop elements
a.pop()
print(a)
#clear elements
a.clear()
print(a)
b.clear()
print(b)

#set operations
A={1,2,3,4,5}
B={2,6,7,8,3}
#union
print(A | B) #method 1
print(A.union(B)) #method 2
 
#intersection
print(A&B) #method 1
print(A.intersection(B)) #method 2

#difference
print(A-B) #method 1      
print(A.difference(B)) #method 2
"""difference displays elements which are in set a but not in b while 
symmetric difference displays elements present in a and b but not the common elements"""

#symmetric difference
print(A^B) #method 1
print(A.symmetric_difference(B)) #method 2

#membership 
print(2 in A)

#dictionaries
student={"name":"aarav","age":21,"is_adult":True}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
print(student["name"])#access value
student["college"]="ssit"
print(student)
student.update({"branch":"aiml","place":"karnataka"})
print(student)
del student["place"]
print(student)
#modify value
student["branch"]="is"
print(student)

#conditional statements
#if-else
age=20
if age>=18:
    print("eligible to vote")
else:
    print("not eligible.")

#if-elif-else
marks=85
if(marks>=85):
    print("distinction")
elif(marks>=75):
    print("first class")
elif(marks>=65):
    print("second class")
elif(marks>=35):
    print("pass")
else:
    print("fail")

#nested if
age=20
place="karnataka"
is_citizen=True
if(age>18):
    if(is_citizen):
        if(place):
            print("eligible to vote")
        else:
            print("not eligible")

#using operators
if(age==20) and place=="karnataka":
    if(is_citizen):
        print("vote")
else:
    print("not eligible")

#for loop
fruits=["apple","orange","strawberry"]
for fruit in fruits:
    print(fruit)


#table
number=int(input("enter an integer:"))
for count in range(1,11):
    multiple=number*count
    print(number, "X",count, "=",multiple)

#sum of 1-100
total=0
for i in range(1,101):
    total+=i
    if(i==100):
        print(i,end="")
    else:
        print(i,end="+")

#nested for loop
for i in range(5):
    for j in range(5):
        print(i,j)

#while loop
count=1
while count<=10:
    print(count)
    count=count+1

#break
for i in range(1,6):
    if(i==4):
        break
    print(i)

#continue
for i in range(1,6):
    if(i==4):
        continue
    print(i)

#pass
for i in range(1,6):
    if(i==4):
        pass
    print(i)