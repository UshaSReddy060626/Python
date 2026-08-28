#single inheritance
class Person:
    def show(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("I am studying")

s = Student()
s.show()      
s.study()

#multilevel inheritance
class Person:
    def show(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("I am studying")

class CollegeStudent(Student):
    def project(self):
        print("I am doing a project")

c = CollegeStudent()
c.show()       
c.study()      
c.project()    


#multiple inheritance
class Father:
    def work(self):
        print("Father goes to work")

class Mother:
    def cook(self):
        print("Mother cooks food")

class Child(Father, Mother):
    def play(self):
        print("Child plays")

c = Child()
c.work()     
c.cook()      
c.play()     