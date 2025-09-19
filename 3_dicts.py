# Dictionaries: key-value pairs, unordered, mutable

mydict = {"name": "me", "age": 7, "city": "mars"}
print(mydict)

# Creating a dictionary using the dict built-in function
mydict2 = dict(name="meee", age=77, city="marss")  
# print(mydict2)

# Accessing the value using the key "name"
value = mydict["name"]  
# print(value)

# Adding a new key-value pair to mydict
mydict["email"] = "me.com"  
# print(mydict)

# Deleting a key-value pair from mydict
# del mydict["city"]  
# print(mydict)

mydict3 = {"name": "meeee", "age": 7, "city": "maarrs"}
# print(mydict3)

mydict3.pop("name")  # Removing a specific key-value pair using the key
# print(mydict3)

mydict3.popitem()  # Removing the last key-value pair from mydict3
# print(mydict3)

# try:
#     print(mydict3["age"])
# except KeyError:
#     print("Key not found")

# Iterating through key-value pairs in mydict3
# for key, value in mydict3.items():
#     print(key, value)

# Creating a shallow copy of mydict3
mydict3_cpy = mydict3  # Shallow copy shares the same memory, changes in one affect the other

# Creating a deep copy of mydict3
mydict3_cpy = mydict3.copy()  # Deep copy does not affect the original dictionary
mydict3_cpy = dict(mydict3)
mydict3_cpy["email"] = "meee.com"
# print(mydict3_cpy)
# print(mydict3)

# Merging dictionaries using the update method
mydict3 = {"name": "meeee", "age": 7, "city": "maarrs"}
mydict4 = {"name": "meeee", "age": 7, "email": "mee.comm"}
mydict3.update(mydict4)
# print(mydict3)

# Note: Dictionaries can use integers and tuples as keys, but not lists
