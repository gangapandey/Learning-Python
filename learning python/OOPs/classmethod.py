# static methos cannont acess or modify class state and generally for utility.

class Person:
    name = "anonymus"

    @classmethod
    def changeName (cls, name):
        cls.name = name

p1 = Person()
p1.changeName("RahulKumar")
print(p1.name)
print(Person.name)