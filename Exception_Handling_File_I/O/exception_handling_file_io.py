#exception handling 
#value error

try:
   marks="ten"
   total=int(marks)
   print(total)
except ValueError:
    print("please enter numbers only.")

#zero division error
num=int(input("enter a number:"))
try:
    print(num/0)
except ZeroDivisionError:
    print("entered number cant be divided by zero.")

#file not found error
try:
        with open("toy.py","r") as file:
            content=file.read()
except FileNotFoundError:
        print("create a new file ,previous file does not exist")

#index error
try:
     color=["blue","white","pink"]
     print(color[3])
except IndexError:
     print("the index does not exist.")

#key error
try:
     info={"aarav":21,"vansh":20,"indu":23}
     value=info["keerthi"]
except KeyError:
     print("keerthi does not exist in the info")


#multiple except blocks
try:
     number=int(input("enter a number:"))
     print(number/100)
except ValueError:
     print("enter numbers only.")
except ZeroDivisionError:
     print("number is not divisble by zero.")

#exception as e
num=int(input("enter a number:"))
try:
    print(num/0)
except Exception as e:
    print(e)

#finally
num=50
try:
     print(num/0)
except:
     print("error")
finally:
     print("program exceuted")
    
#raise statement
age=16
if age<=18:
     raise Exception("not adult.")

#custom error
class salarytoolow(Exception):
     pass
try:
        salary=5000
        if salary<=20000:
            raise salarytoolow("salary too low.")
except salarytoolow as error:
     print(error)