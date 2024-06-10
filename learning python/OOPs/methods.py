class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to python world ", self.name)
    def getMarks(self):
        return self.marks
        
s1 =  student ("Karan", 98)
s1.welcome()
s1.getMarks()
print(s1.getMarks())

# Create student class that takes name and marks of 3 subject as argument in constructor and create method to print avg
class stud:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0 
        for val in self.marks:
            sum = sum + val
            print ("Hi, ", self.name, "marks = ", sum/3)

s2 = stud("Tony", [99, 98, 97])
s2.avg()


# -------- Static Method ----
class emp:
    @staticmethod
    def company():
        print("ABC Company")