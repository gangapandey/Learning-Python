# open read and close file
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# WAP to create a new file in 'practice.txt' using Python and add the following data
# Hi all
# We are learning file I/O
with open("practice.txt", "w") as f:
    f.write("Hello all \n we are learning file I/O")


# write a file that replace all occourences of python with java in above file.
with open("practice.txt", "r")as f:
    data = f.read()
new_data = data.replace("Python", "Java")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# WAP to search if word 'learning' exists in the file or not.
word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print ("found")
    else:
        print("not found")

# WAF to find in which line of the file does the word "learning" occours first. Print - 1 if word not found
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        daya = data.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data.readline()
            if (word in data):
                print(line_no)
                return
            line_no + 1
            return -1
        
        print (check_for_line())