# Strings: ordered, immutable, used for text representation

myString = "I am  '  '  . yep "
#print(myString)

myString1 = "hello world!"
#char = myString1[0]  # Accessing a character by index (also supports negative indexing)
#print(char)

slicing = myString1[2:6]  # Slicing a string to get a substring
#print(slicing)

concatenatingString = myString1 + "   " + myString  # Concatenating strings
#print(concatenatingString)

for i in myString1:
    print(i)  # Iterating through characters in a string

if 'ello' in myString1:
    print("Yes")
else:
    print("No")

# Additional string methods:

# len(myString1)  # Returns the length of the string
# myString1.upper()  # Converts the string to uppercase
# myString1.lower()  # Converts the string to lowercase
# myString1.strip()  # Removes leading and trailing whitespace
# myString1.replace("hello", "hi")  # Replaces a substring with another
# myString1.split()  # Splits the string into a list of substrings
# ",".join(["hello", "world"])  # Joins a list of strings into a single string
# myString1.startswith("he")  # Checks if the string starts with a specific substring
# myString1.endswith("!")  # Checks if the string ends with a specific substring
# myString1.find("l")  # Returns the index of the first occurrence of a substring
# myString1.index("l")  # Returns the index of the first occurrence of a substring (raises an error if not found)
# myString1.count("l")  # Counts the number of occurrences of a substring

# String formatting:
# name = "Ali"
# age = 20
# print(f"My name is {name} and I am {age} years old.")  # f-strings (Python 3.6+)
# print("My name is {} and I am {} years old.".format(name, age))  # Format method
# print("My name is %s and I am %d years old." % (name, age))  # Old-style formatting

# Strings are immutable, meaning you cannot modify individual characters. However, you can create a new string by concatenating, slicing, or using other string methods.
