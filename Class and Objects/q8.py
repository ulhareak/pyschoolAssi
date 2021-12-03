"""
Inheritance allows the reuse of code, by implementing
a parent-child relationship between classes. Create 2 derived classes
Student and WorkingAdult from the base class Person.

Examples

    >>> s = Student('Peter', 9, 'ABC Primary School')
    >>> s.introduce()
    'My name is Peter. I am 9 years old. I am studying at ABC Primary School.'
    >>> a = WorkingAdult('John', 23, 'Waiter')
    >>> a.introduce()
    'My name is John. I am 23 years old. I am a waiter.'
"""
class Person:
      """A base class"""
      def __init__(self, name, age):
          self.name = name
          self.age = age

class Student(Person):
      """A derived class for Student"""
      def __init__(self, name, age, school):
          Person.__init__(self, name, age)
          self.school = school

      def introduce(self):
      	return 'My name is {}. I am {} years old. I am studying at {}.'.format(self.name , self.age, self.school)


class WorkingAdult(Person):
      """A derived class for WorkingAdult"""
      def __init__(self, name, age, job):
      	Person.__init__(self ,name , age  )
      	self.job = job.lower()

      def introduce(self):
      	return 'My name is {}. I am {} years old. I am a {}.'.format(self.name , self.age, self.job)

s =Student("avdhut", 24, "SPPU")
w =WorkingAdult("Avdhut"  ,24 , "Amazatic LLC")
print(s.introduce())
print(w.introduce())
      	
