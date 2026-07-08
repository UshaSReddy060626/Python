#string
def greet(name:str)->str:
    return "hi "+name
friend="Aarav"
print(greet(friend))

#list
from typing import List
names:List[str]=["Aarav","shreshta"]
for n in names:
    print(f"hello {n}")

#dictionary
from typing import Dict
marks:Dict[str,int]={
    "math":95,
    "social":90
} 
print(marks)

