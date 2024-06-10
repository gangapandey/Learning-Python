# class Car:
#     color = "black"

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# # Create instances of Toyota
# car1 = Toyota("Fortuner")
# car2 = Toyota("Suzuki")

# print("Car1 name:", car1.name)
# print("Car2 name:", car2.name)

# # Start and stop car
# car1.start()
# car2.stop()

# # Print the color of the cars
# print("Car1 color:", car1.color)
# print("Car2 color:", car2.color)


# -------- MULTI-LEVEL INHERITANCE -----------------
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(Toyota):
    def __init__(self, type):
        self.type = type

car11 = fortuner("disel")
car11.start()


# ---------------- MULTIPLE INHERITANCE --------------
class A:
    varA = "welcome to class a"
class B:
    varB =  "welcome to group B"
class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)