a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
print("-"*50)
print("select your choice")
print("-"*50)
print("1:for addition\n2: for subtraction\n3:for multiplication\n4:for division\n5:for floor division\n6:for exponentiation")
print("-"*50)
choice=input("Enter your Choice.eg(1...6)")
operator={
    "1":a+b,
    "2":a-b,
    "3":a*b,
    "4":a/b,
    "5":a//b,
    "6":a**b
}
print("Result:",operator[choice])



