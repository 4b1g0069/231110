class Student:
    def _init_(self, stu_name , stu_id):
        self.stu_name = stu_name
        self.stu_id = stu_id
    
    def _stf_(self):
       return f"Name:{self.stu_name}\nId={self.stu_id}"
    def addCourse(self , object)

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def _str_(self):
        return f"Name:{self.name}\nAge={self.age}"

p1 = Person("John",36)
print(p1)

p2 = Person("Sue",22)
print(p2._dict_)
