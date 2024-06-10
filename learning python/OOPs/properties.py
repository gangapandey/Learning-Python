# when the value of an attribute depends upon function, we can make that function property/attribute.

class Student:
    def __init__(self, phy, chem): 
        self.phy = phy
        self.chem = chem

    @property
    def percent(self):
        return str((self.phy + self.chem) / 2) + "%"
    
stu1 = Student(99, 97)
print(stu1.percent)
stu1.phy = 87
print(stu1.percent)
