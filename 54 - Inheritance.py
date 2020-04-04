class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isStudent(self):
        return False


class Student(Person):
    def isStudent(self):
        return True


emp = Person("Person1")
print(emp.getName(), emp.isStudent())
emp = Student("Person2")
print(emp.getName(), emp.isStudent())