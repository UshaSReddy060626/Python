class Student:
    school = "ABC Public School"
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid Marks!")
    @classmethod
    def show_school(cls):
        print(cls.school)
    @staticmethod
    def check_pass(marks):
        return marks >= 35
    def __str__(self):
        return f"Name: {self.name}, Marks: {self._marks}"
s = Student("Usha", 90)
Student.show_school()
print(s)
if Student.check_pass(s.marks):
    print("Passed")
else:
    print("Failed")
s.marks = 120
print(s)