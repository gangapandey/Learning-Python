# --------- WHILE LOOP -------------
# count = 1
# while count <= 5:
#     print("Hello")
#     count +=1

# WAP to print i*i
# i = 1
# while i <= 5:
#     print (i*i)
#     i +=1

# WAP to print 5 to 1
# i = 5
# while i >= 1:
#     print (i)
#     i = i - 1

#  WAP to print number from 1 to 100
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1

# WAP to print number from 100 to 1
# i=100
# while i >= 1:
#     print(i)
#     i = i - 1

# WAP to print multiplication table of number n
# n = int(input("Enter number:"))
# i = 1
# while i <= 10:
#     print(str(n) + "*" + str(i) + "=" + str(n*i))
#     i = i + 1

# WAP to print elements of following list using a loop [1,4,9,16,25,36,49]
# i=0
# num = [1,4,9,16,25,36,49]
# while i < len(num):
#     print(num[i])
#     i = i+1


# ------ BREAK AND CONTINUE -----------
# i = 1
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i = i + 1

# i = 0
# while i <= 5:
#     if (i == 3):
#         i = i + 1
#         continue
#     print(i)
#     i = i+1


# ---------------- FOR LOOP -------------------------
# num = [1,2,3,4,5]
# for val in num:
#     print(val)


# WAP to print each character of the string until it finds the letter 'o'
# str = "Hello Maya"
# for char in str:
#     if(char == 'o'):
#         print("O found")
#         break
#     print(char)
# else:
#     print("End")

# WAP to print elements of following list using a loop [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)

# WAP to search for number x in tuple by loop (1,4,9,16,25,36,49,64,81,100)
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
for val in nums:
    if (val == x):
        print("number found")
     