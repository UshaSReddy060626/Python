try:
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    result=num1/num2
    print("result=",result)
except ZeroDivisionError:
    print("error,division by zero")
except ValueError:
    print("please enter numbers only")