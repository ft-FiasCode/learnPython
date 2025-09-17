# Tuples: a collection data type, ordered, immutable, allows duplicate data,
# similar to a list, but cannot be changed after its creation.
mytuple = ("me", 7, "mars") 
print(mytuple)

# Tuples can work without parentheses, like: mytuple = "me", 7, "mars"
# If a tuple has only one element, it is considered a string, but if a comma ',' is added at the end, it becomes a tuple.

mytuple1 = tuple([True, "me", 7, "mars"])  # Converting a list to a tuple
# print(mytuple1)

item = mytuple1[2]  # Accessing an element by index, also supports negative indexing
# print(item)
# print(mytuple1.index("mars"))  # Using the .index() method to find the index of an element
# print(mytuple1.count("me"))  # Using the .count() method to count the occurrences of an element

# Iterating through a tuple
# for i in mytuple1:
#     print(i)

# Tuple unpacking
mytuple2 = "me", 7, "mars"
name, age, city = mytuple2  # The number of variables must match the number of elements in the tuple
# print(name)
# print(age)
# print(city)

# Partial unpacking with the * operator
mytuple3 = (1, 2, 3, 4, 5)
i1, i2, *i3 = mytuple3
# print(i1)
# print(i2)
# print(i3)  # The remaining elements are unpacked into a list

# Comparing tuples and lists:
# Tuples are immutable, so they are more efficient than lists, especially when working with large data, due to Python's internal optimization.
import sys
list_example = [1, 2, 3, "hello", True]
tuple_example = (1, 2, 3, "hello", True)
# print(sys.getsizeof(list_example), "bytes")
# print(sys.getsizeof(tuple_example), "bytes")

# Tuples are also more efficient in terms of iteration and creation compared to lists.
import timeit
# print(timeit.timeit(stmt="[1,2,3,4,5]", number=100000))  # List
# print(timeit.timeit(stmt="(1,2,3,4,5)", number=100000))  # Tuple
