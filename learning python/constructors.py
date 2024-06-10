class student:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty
        print("Adding new students...")

s1 = student("Karan", "tech")
s2 = student("Arjun", "finance")
print(s1.name, s1.faculty)
print(s2.name, s2.faculty)


# --------- Default constructor ------------
class demo:
    def __init__(self):
        print("default constructor calling.......")

obj = demo()


# --------------- Parameterized Constructor -------------
class demoo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s11 = demoo("ram", 22)
print(s11.name, s11.age)



