# list is an ordered sequence of items. All items in list donot need to be of same datatype.
# Lists: ordered, mutable, allow duplicate data

# Original list
mylist = ["apple", "cherry", "banana", "orange", "pear", "kiwi"]
print(mylist)

# Create a copy of mylist
mylist2 = list(mylist)
#print(mylist2)

# List with duplicates and additional items
mylist3 = [3, True, "apple", "apple", "melon", 4.5, "grape"]
#print(mylist3)

item1 = mylist3[-2]  # Last index
#print(item1)

# Loop through and print all items in mylist3
for i in range(mylist3):
    print(i)

# Length of mylist3
#print(len(mylist3))

# Append "lemon" to mylist3
mylist3.append("lemon")
#print(mylist3)

# Remove and return the last item in mylist3
item2 = mylist3.pop()
#print(mylist3)

# Reverse the order of elements in mylist3
mylist3.reverse()
#print(mylist3)

# Clear all items from mylist3
mylist3.clear()
#print(mylist3)

# Sort mylist4 in place
mylist4 = [1, 5, 4, 3, 2, -9]
mylist4.sort()
#print(mylist4)

# Create a sorted copy of mylist4
mylist5 = sorted(mylist4)
#print(mylist5)

# Create a list of zeros with length 4
mylist6 = [0] * 4
#print(mylist6)

# Concatenate mylist6 and mylist7
mylist7 = [1, 2, 3, 4]
mylist8 = mylist6 + mylist7
#print(mylist8)

# Slice mylist9 to get a sublist with 5 elements
mylist9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
mylist10 = mylist9[1:6]
#print(mylist10)

# Slice mylist9 to skip every other element
mylist11 = mylist9[::2]
#print(mylist11)

# Reverse the order of elements in mylist9
mylist12 = mylist9[::-1]
#print(mylist12)

# Square each element in mylist13 using list comprehension
mylist13 = [1, 2, 3, 4, 5]
mylist14 = [i * i for i in mylist13]
#print(mylist14)
