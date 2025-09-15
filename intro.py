# Python Basics

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

# End