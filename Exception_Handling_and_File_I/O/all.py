class invalidageerror(Exception):
    pass
try:
    age=int(input("enter your age:"))
    if age<=18:
        raise invalidageerror("you are not eligible to vote.")
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    print("division:",num1/num2)
except invalidageerror as e:
    print(e)
except ZeroDivisionError:
    print("error,division by zero")
except ValueError:
    print("please enter numbers only")
finally:
    print("program executed successfully.")