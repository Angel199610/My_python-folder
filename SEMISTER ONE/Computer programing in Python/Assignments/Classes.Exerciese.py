#Printing user's name and age
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello I leave in Bweyogerere" + self.location)

p1 = Person("Angel", 36)

p1.age = 36
p1.name = "Angel"

print(f"My Name is {p1.name} and I am {p1.age} years old")


#Printing User's location
class Person:
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("Hello I leave in Bweyogerere" + self.location)

p1 = Person("Angel", 36)

p1.name = "Angel"
p1.location = "Bweyogerere"

print(f"I leave in {p1.location}")
