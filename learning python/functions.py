def calsum(a,b):
    sum = a + b
    print(sum)
    return(sum)
calsum(3,4)

# WAP to calculate average of 3 numbers using function
def calavg(a,b,c):
    avg = (a+b+c)/3
    print("Your average is ", avg)
    return(avg)
calavg(4,5,6)

# WAP to use default parameter
def calsum(a = 4, b = 4):
    sum = a+b
    print("The sum is ", sum)
    return(sum)
calsum()

# WAP to print the lenght of list (list is a parameter)
foods = ["momo", "pizza", "burger", "pasta"]
def print_len(list):
    print(len(list))

print_len(foods)

# WAP to print element of a list in a single line (list is a parameter)
foods = ["momo", "pizza", "burger", "pasta"]
def print_list(list):
    print(list)

print_list(foods)

# WAP to find the factorial of n (n is the parameter)
num = int(input("enter number:  "))
def get_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        print(" Factorial is ", fact)
get_fact(num)

# WAP to check whether entered number is odd or even using function
num = int(input("Enter number: "))
def check_num(n):
    if (n % 2 == 0):
        print("The number is even")
    else:
        print("the number is odd")

check_num(num)


# WAP to convert USD in NPR
def convert(usd_val):
    npr_val = usd_val*120
    print("in npr = ", npr_val)
convert(30)


# ------------ Recursion ------------------

def show(n):
    if ( n == 0):
        return
    print(n)
    show(n-1)
show(5)

# WAP to find factorial in recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

result = fact(5)
print("Factorial:", result)

# Write a recursive function to calculate sum of first n natural number
def calc_sum(n):
    if (n == 0):
        return 0
    else:
        return calc_sum(n-1) + n
    
sum = calc_sum(5)
print(sum)

# Write a recursive function to print all element in the list (list and index are parameter)
def print_list(list, indx):
    if (indx == len(list)):
        return
    print(list[indx])
    print_list(list, indx + 1)

fruit = ["apple", "banana", "chhery", "mango"]
print_list(fruit, 0
)