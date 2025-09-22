# Collection: Counter, namedtuple, OrderedDict, defaultdict, deque
# The collections module implements special container data types and provides additional
# functionality compared to built-in containers.

from collections import Counter

# Example 1: Counting the occurrences of characters in a string
a = "aaaabbbcccdddddddd"
myCounter = Counter(a)
# print("Counts of each unique character in the string:")
# print(myCounter)

# Example 2: Counting the occurrences of words in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
wordCounter = Counter(words)
# print("\nCounts of each word in the list:")
# print(wordCounter)

# Example 3: Counting the frequency of characters in a sentence
sentence = "Python is a powerful programming language"
charCounter = Counter(sentence)
# print("\nCounts of each character in the sentence:")
# print(charCounter)

# Example 4: Finding the most common elements in a list
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
numberCounter = Counter(numbers)
mostCommon = numberCounter.most_common(2)  # Get the 2 most common elements
# print("\nMost common elements in the list:")
# print(mostCommon)

# Arithmetic Operations with Counters
c1 = Counter("abcdef")
c2 = Counter("bcdefgh")

# Addition (+)
c3 = c1 + c2
# print("\nAddition (+):")
# print(c3)

# Subtraction (-)
c4 = c1 - c2
# print("\nSubtraction (-):")
# print(c4)

# Intersection (&)
c5 = c1 & c2
# print("\nIntersection (&):")
# print(c5)

# Accessing Elements in a Counter
# print("\nAccessing Elements:")
# print(c1["a"])  # Output: 1
# print(c1["x"])  # Output: 0 (non-existing key returns 0)

# Updating and Manipulating Counts
# print("\nUpdating and Manipulating Counts:")
c6 = Counter("hello")
c6.update("world")  # Add counts from another Counter
# print(c6)

del c6["l"]  # Delete an element from the Counter
# print(c6)

# Additional Operations
# print("\nAdditional Operations:")
# print(c6.most_common(2))  # Get the 2 most common elements
# print(+c6)  # Get items with positive counts
# print(-c6)  # Get items with negative counts (empty in this case)
