#comments in python
#This is a single line comment
"""this is a multi 
line comment
in python"""

#variables in python
place="manali"
a,b,c=8,"blue",78.0

#datatypes in python
student_id=30
weight=55.7
message="Hi Welcome"
is_light_on=True
coordinates=4+3j

#type casting in python
print(type(student_id))
print(type(weight))
print(type(message))
print(type(is_light_on))
print(type(coordinates))


#print statement in python
print(student_id)
print(weight)
print(message,is_light_on,coordinates)

#input in python
name=input("enter your name:")
roll_no=int(input("enter your roll no:"))
college=input("enter your college name")
branch=input("enter your branch name")
#f-string and format
print("name{},roll_no{},college{}".format(name,roll_no,college))
print(f"name:{name}\nroll_no:{roll_no}\ncollege:{college}\nbranch name:{branch}")

# operators
# arithematic operators
a=2
b=5
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("square root",a**b)

#relational operators
print("is a==b:",a==b)
print("a is not equal to b:",a!=b)
print("is a greater than b:",a>b)
print("is b less than a:",b<a)
print("is a less than or equal to b:",a<=b)
print("is b greater than or equal to a",b>=a)

#logical operators
c=40
d=40
print((c==d) and (c==d))
print((c>=d) or (d<=c))
print(not (c==d) )

#bitwise operators
print(c & d)
print(c |d)
print(c^d)
print(~c)

# assignment operators
a+=5
print("a=",a)
b-=2
print("b=",b)
a*=3
print("a=",a)
b/=2
print("b=",b)

#membership operators
text="nice to meet you"
print("you" in text)
print("hello" not in text)

#identity operators
color_a=["red","blue"]
color_b=["red","blue"]
print(color_a is color_b)
print(color_a is not color_b)

