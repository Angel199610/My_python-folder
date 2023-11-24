"Python Classes"
#A Class is like an object constructor, or a "blueprint" for creating objects.

"How to create a Class"
#We use the keyword class:
class MyClass:
  Angel = 27

print(MyClass)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Angel", 36)

print(p1.name, p1.age)