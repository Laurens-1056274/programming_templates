# Python: make a class/classes
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, my name is " + self.name

""" To use this in a different file: use

from [name_file] import [class name]

name = "Jacob"
introduction = Person(name).greet()
print(introduction)

"""