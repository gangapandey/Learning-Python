info = {
    "name": "Adrena",
    "age": 20,
    "address": "London",
    "marks" : 98,
    "is_adult": True
}
print(info)
print(info['name'])
print(len(info))
x = info.get("address")
print(x)

# Adding new item in dictionary
info["currently in"] = "Ktm"
print(info)

# Removing item from dictionary
info.pop("address")
print(info)


# --------- Neested Dictionaries ----------
stud = {
    "name" : "Sita",
    "age" : 13,
    "score": {
        "phy" :20,
        "chem" :25,
        "maths" :30
    }
}
print(stud)
print(stud["score"]["maths"])


# --------- Dictionary Methods ---------

# info.keys(): returns all the keys
print(info.keys())
print(list(info.keys()))

# info.values(): returns all the values of keys
print(info.values())

# info.items(): returns all (kay val) pairs as tuples
pair = list(info.items())
print(pair[0])

# info.get(): returns the key according to value
print(info.get("name"))

# info.update(new_dict): insert the specified item to dictionary
new_dict = {"city" : "Kathmandu"}
info.update(new_dict)
print(info)


# --------- Questions -----------

# WAP to store the following word meanings in python dictionary table: "a piece of furniture", " list of facts", cat: "a small animal"
mydict = {
    "cat" : " a small animal",
    "furniture": {
        "a piece of furniture",
        " alist of facts"
    }
    }
print(mydict)


# You are given list of subjects for students. Assume one classroom is required for  1 subjects. How many classroom are needed for all students?
#  "python", "java", "c", "java", "python"
subjects = {
    "python", "java", "c", "java", "python"
}
print(len(subjects))


# WAP to enter marks of 3 subjects and store them in dictionary. start with empty dictionary and add one by one.
marks = {}
x = int (input("Enter phy marks :"))
marks.update({"phy" : x})
y = int (input("Enter chem marks :"))
marks.update({"chem" : y})
z = int (input("Enter comp marks :"))
marks.update({"comp" : z})
print(marks)


