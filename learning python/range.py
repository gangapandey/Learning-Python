# Range function returns a sequence of numbers, starting from 0 by default and increment by 1 (by default) and stops before a specified number.

# WAP to generate a sequence of numbers from 0 to 4 using the range(5) function and print each number in the sequence.
seq = range(5)
for i in seq:
    print(i)

# WAP to print numbers from 0 to 9 using the range(10) function.
for i in range(10):
    print(i)

# WAP to print numbers from 2 to 9 using the range(2, 10) function.
for i in range(2, 10):
    print(i)

# WAP to print every second number from 2 to 8 using the range(2, 10, 2) function.
for i in range (2,10,2):
    print(i)

# WAP to print number from 1 to 100 using for and range
num = range (1, 101)
for i in num:
    print(i)

# WAP to print number from 100 to 1 using for and range
num = range (100, 0, -1)
for i in num:
    print(i)

# WAP to print the multiplication table of number n
n = int(input("enter number :"))
for i in range(1,11):
    print(n*i)