#counter
from collections import Counter
fruits=["apple","mango","guava","apple","apple","chiku"]
count=Counter(fruits)
print(count)
print(count["apple"])
print(count.most_common(1))

#default-dict
from collections import defaultdict
students=defaultdict(list)
students["python"].append("AARAV")
students["python"].append("SHRESHTA")
students["maths"].append("GAYU")
print(students)

#deque
from collections import deque
a=deque([1,2,3])
print(a)
a.append(4)
print(a)
a.appendleft(10)
print(a)
a.popleft()
print(a)

#named tuple
from collections import namedtuple
student=namedtuple("student",["name","age","branch"])
s=student("Aarav",20,"AIML")
print(s.name)
print(s.age)
print(s.branch)

#regex
import re
a="my number is 909098988"
result=re.search(r"\d+",a)
print(result.group())


#date-time
from datetime import datetime
now=datetime.now()
print(now)
print(now.date())
print(now.time())
print(now.year)

#type hints
def add(a:int,b:int)->int:
    return a+b
a=8
b=9
result=add(a,b)
print(result)

#optional and union
# optional
from typing import Optional
phone:Optional[str]=None



#union 
from typing import Union
id:Union[int|str]=1234
print(f"your id is a number:{id}")
id:Union[int|str]="23AI053"
print(f"your id is a combination of no's and characters:{id}")

#logging
import logging
logging.basicConfig(
filename="a.log",
level=logging.INFO)
logging.info("program started")

#virtual environment
#for windows
"""python -m venv myenv
to activate:
myenv\Scripts\activate
deactivate:
deactivate
"""
#pip commands
"""
install package:
pip install package_name
uninstall:
pip uninstall package_name
upgrade:
pip install --upgrade package_name
list installed packages:
pip list
show package details:
pip show package_name
freeze packages:
pip freeze
save dependencies:
pip freeze > requirements.txt
install from requirements:
pip install -r requirements.txt
"""
# pipenv 
"""Install pipenv
pip install pipenv
Create environment
pipenv install
Install package
pipenv install requests
Activate environment
pipenv shell
Exit environment
exit
 Remove environment
pipenv --rm"""