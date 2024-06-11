# Define a circle class to create a circle with radius r using constructor.Dine area() method of class which calculates area of circle. Define Perimeter() method of class which allows you to calculates perimeter of circle
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return (22/7)* self.radius **2 
    
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1 = Circle(21)
print("Area of circle = ", c1.area())
print("Perimeter of circle = ", c1.perimeter())


# Define a employee class with attribute role, department, and salary. This class also has a showDetails() method.
# Create an engineer class that inherits properties from employee and 
class Employee:
    def __init__(self, role, depart, salary):
        self.role = role
        self.depart = depart
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("depart = ", self.depart)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

    def showDetails(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        super().showDetails()

Emp = Employee("HR", "Finance", "400000")
Emp.showDetails()

E1= Engineer("Rahul Pandey", 22)
E1.showDetails()


# Create a class called order which stores items and its price. Use dunder function __gt__() to convey that
# Order1 > Order2
# if price of order1 > price of order2 

class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, other):
        return self.price > other.price
    
ord1 = Order("chips", 20)
ord2 = Order("tea", 10)
print(ord1 > ord2)
