
    
class Student:
    def _init_(self, stu_name , stu_id):
        self.stu_name = stu_name
        self.stu_id = stu_id

    

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
