# WAP to check the lights in traffic
light = "yellow"
if(light == "red"):
    print("you've to stop")
elif(light == "green"):
    print("you've to go")
elif(light == "yellow"):
    print("you've to look")
else:
    print("light is broken")


# Neesting conditional statement
age = 95
if (age >= 18):
    if (age >= 80):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You're small")


# # WAP to check number entered by user is odd or even.
num = int(input("Enter the number:"))
if (num % 2 == 0):
    print("number is even")
else:
    print("number is odd")


# # WAP to find greatest of 3 number entered by user.
n1 = int(input("Enter the 1st number:"))
n2 = int(input("Enter the 2nd number:"))
n3 = int(input("Enter the 3rd number:"))
if (n1 > n2 and n1 > n3):
    print("N1 is greatest")
elif(n2 > n1 and n2 > n3):
    print("N2 is the greatest")
else:
    print("N3 is the greatest")


# # WAP to check if a number is multiplied by 7 or not 
num = int(input("Enter the number:"))
if (num % 7 == 0):
    print("number is multiplied by 7")
else:
    print("number is not multiplied by 7")
