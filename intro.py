# --------------------------------------------------
# 1. Comments
# --------------------------------------------------
# Single line comments start with a hash symbol (#).
# They help explain what the code does.

"""
Multiline comments or documentation can be written
using triple quotes. This is useful for longer explanations.
"""

# --------------------------------------------------
# 2. Numbers and Math Operations
# --------------------------------------------------
# You can just write numbers in Python:
3  # This is a number

# Basic math operations:
print(1 + 1)   # Addition: 2
print(8 - 1)   # Subtraction: 7
print(10 * 2)  # Multiplication: 20
print(35 / 5)  # Division: 7.0 (division always returns a float)

# Floor division (rounds down to nearest whole number):
print(5 // 3)   # 1
print(-5 // 3)  # -2

# Modulo gives the remainder:
print(7 % 3)    # 1 (7 divided by 3 leaves remainder 1)

# Exponentiation (power):
print(2 ** 3)   # 8 (2 to the power of 3)

# Use parentheses to control order of operations:
print(1 + 3 * 2)    # 7 (multiplication before addition)
print((1 + 3) * 2)  # 8 (parentheses change order)

# --------------------------------------------------
# 3. Boolean Values and Logic
# --------------------------------------------------
# Boolean values can be True or False (first letter capitalized):
print(True)
print(False)

# You can negate them with 'not':
print(not True)   # False
print(not False)  # True

# Logical operations:
print(True and False)  # False (and means both must be True)
print(False or True)   # True (or means one of them is True)

# Boolean values behave like numbers (True=1, False=0):
print(True + True)   # 2
print(True * 8)      # 8
print(False - 5)     # -5

# --------------------------------------------------
# 4. Comparisons
# --------------------------------------------------
print(1 == 1)   # True (equal to)
print(2 != 1)   # True (not equal to)
print(1 < 10)   # True (less than)
print(2 >= 2)   # True (greater than or equal to)

# You can chain comparisons:
print(1 < 2 < 3)  # True

# 'is' checks if two variables point to the same object:
a = [1, 2, 3]
b = a
print(b is a)   # True (same object)
b = [1, 2, 3]
print(b is a)   # False (different objects with same values)
print(b == a)   # True (values are equal)

# --------------------------------------------------
# 5. Strings
# --------------------------------------------------
# Strings can use double or single quotes:
print("Hello")
print('World')

# Strings can be combined with +:
print("Hello " + "World!")

# Strings can be indexed like lists:
print("Hello"[0])  # H

# Find length of a string:
print(len("Hello"))

# You can use f-strings for formatted text:
name = "ft-FiasCode"
print(f"Her name is {name}.")
print(f"{name} has {len(name)} letters.")

# --------------------------------------------------
# 6. None (Special Value)
# --------------------------------------------------
# None is used to represent 'no value' or emptiness:
print(None)

# Always use 'is' to compare with None:
print(None is None)      # True
print("text" is None)    # False

# --------------------------------------------------
# 7. Lists - Ordered, Mutable
# --------------------------------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits)           # ['apple', 'banana', 'cherry']
print(fruits[0])        # apple (indexing)
fruits.append("orange") # Add item
print(fruits[-1])       # orange (last item)
fruits[1] = "kiwi"      # Modify
print(fruits)           # ['apple', 'kiwi', 'cherry', 'orange']

# --------------------------------------------------
# 8. Tuples - Ordered, Immutable
# --------------------------------------------------
point = (10, 20)
print(point[0])         # 10
# point[0] = 5         # ERROR! Tuples can't be changed

coords = (1, 2), (3, 4) # Tuple of tuples
print(coords)           # ((1, 2), (3, 4))

# --------------------------------------------------
# 9. Dictionaries - Key-Value Pairs
# --------------------------------------------------
person = {
    "name": "ft-FiasCode",
    "age": 20,
    "city": "NYC"
}
print(person["name"])   # ft-FiasCode
person["job"] = "Dev"   # Add key
print(person)           # {'name': 'ft-FiasCode', 'age': 20, 'city': 'NYC', 'job': 'Dev'}

# --------------------------------------------------
# 10. Sets - Unique, Unordered
# --------------------------------------------------
numbers = {1, 2, 2, 3}  # Duplicates removed
print(numbers)          # {1, 2, 3}
numbers.add(4)
numbers.remove(2)
print(1 in numbers)     # True

# --------------------------------------------------
# 11. Functions
# --------------------------------------------------
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))   # Hello, World!

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))         # 9 (3^2)
print(power(2, 3))      # 8 (2^3)

# *args and **kwargs
def flexible(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

flexible(1, 2, 3, name="ft-FiasCode", age=20)

# --------------------------------------------------
# 12. Classes
# --------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

alice = Person("ft-FiasCode", 20)
print(alice.introduce())

# --------------------------------------------------
# 13. Inheritance
# --------------------------------------------------
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def introduce(self):
        return f"{super().introduce()} in grade {self.grade}"

bob = Student("Bob", 15, 10)
print(bob.introduce())

# --------------------------------------------------
# 14. Properties
# --------------------------------------------------
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value
    
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius, c.area)
c.radius = 10

# --------------------------------------------------
# 15. Collections Module
# --------------------------------------------------
from collections import Counter, defaultdict, namedtuple

# Counter
text = "hello world"
print(Counter(text))

# defaultdict
dd = defaultdict(int)
dd['a'] += 1
print(dd['b'])

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# --------------------------------------------------
# 16. Generators
# --------------------------------------------------
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

# Generator expression
squares = (x**2 for x in range(5))
print(list(squares))

print("Learning Python Complete!")
