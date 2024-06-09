marks = [30, 40, 50, 44, 80]
student1 = ["Ram", 23, "Ktm", True]
print ( student1[0])

# list slicing
marks = [30, 40 , 55, 68, 99, 95, 43]
print(marks[1:4])
print(marks[-3:-1])

# ----- List methods ----------

# list.append(): add element at end of list
list = [30, 40, 20, 60]
list.append(90)
print(list)

# list.sort(): sorts in ascending order
list.sort()
print(list)

# list.sort(reverse=True): sorts in descending order
list.sort(reverse= True)
print(list)

# list.reverse(): reverse the list order
list.reverse()
print(list)

# list.insert(): add element at specified position (first position then number)
list.insert(0, 4)
print(list)

# list.remove(): remove first occourence of element  (value halni ho bracket ma)
list.remove(4)
print(list)

# list.pop(): remove the element of index
list.pop(2)
print(list)

# extend() : append element from another list to current list
a =  ["apple", "banana"]
b = ["strawbeery", "pineapple"]
a.extend(b)
print(a)


# --------- Questions -------

# WAP to ask user to enter name of 3 different movies and store them in list
u1 = input("Enter your fav moviee :")
u2 = input("Enter your fav moviee :")
u3 = input("Enter your fav moviee :")
list = [u1, u2, u3]
print(list)

# WAP to check if list contain palindrome number of element (use copy() method)
newList = [1, 2, 3, 2, 1]
copy_list = newList.copy()
copy_list.reverse()
if (copy_list == newList):
    print("List is palindrome")
else:
    print("List is not palindrome")