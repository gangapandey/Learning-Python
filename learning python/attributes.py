# Attributes are the properties or data associated with an object.

# types of attributes: instance and class attributes

# instance attribute: they are specific to each instance of a class. defined inside constructor ('__init__()' method using self keyword)
class car:
    def __init__(self, name, brand):
        self.name = name                #instance attribute
        self.brand= brand

s11 = car("maruti", "suzuki")
print(s11.name, s11.brand)


# class attribute: they are shared among all instances of class. they are defined outside any method, usually at top of class.
class cars:
    color = "blue"                    #class attribute
    def __init__(self, brand):
        self.brand= brand               

s11 = cars("suzuki")
print(s11.color, s11.brand)