# concatenation of string
a = "Hello"
b = "World"
print ( a + b )
print (a + " " + b)

# length of string
a = "sita"
print (len(a))

# Indexing in string
name = "Interpreter"
ch = str[4]
print(ch)
print(str[6])

# slicing of string
bme = "Hello World"
print(bme [2:5])
print (bme[2:])
print(bme[:5])

#uppercase the string
name = "interpreter"
print(name.upper())

#lowercase the string
name = "interpreter"
print(name.lower())

# replace string
name = "interpreter"
print(name.replace("i", "K"))

# endswith (returns true if the string ends with specified value)
name = "interpreter"
print(name.endswith("ter"))

# capitalize() (converts the first character to uppercase)
name = "interpreter"
print(name.capitalize())

# find()
name = "interpreter"
print(name.find("p"))

# count() (returns number of time a specified value occours in string)
name = "interpreter"
print(name.count("r"))


# WAP to input user's firstname and print its length
name = input("Enter your firstname:")
print(len(name))

# WAP to find the occourence of '$' in string
x = " I am $ USA in $ UK"
print(name.count("$"))