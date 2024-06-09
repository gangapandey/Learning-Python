name = "Ram"
age = 24

print(type(name))
print(type(age))

print ("My name is" + name)
print ("I am" + str(age) + "years old")


# # Taking input from user
yourname = input("Enter name :")
print("Your name is " + yourname)



# # WAP to input two number and print their sum
a = int (input ("enter first number : "))
b = int (input ("enter second number : "))
sum = a + b
print(sum)

# # WAP to input sides of square and print its area
n = int(input("Enter the sides of a square:"))
Area = n ** 2
print ( " sides of square = ", Area)

# # WAP to input two floating point number and find their averages
n1 = float (input ("Enter fist number:"))
n2 = float (input ("Enter second number:"))
avg = (n1 + n2) / 2
print("Average = ", avg)

# #WAP to input two number and print true if a is greater than b
a = int (input ("enter first number : "))
b = int (input ("enter second number : "))
print ( a > b)