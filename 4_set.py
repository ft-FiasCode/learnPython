
# Set: a set can contain any data type, is unordered, mutable, and does not allow duplicates.
# set doesnot support indexing

myset = {1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 8}
#print(myset)

myset = {"ali", "alikhan", "alijan"}
#print(myset)

myset1 = set([1, 2, 3, 4, 3, 4, 5])  # Creating a set using the set function with a list as an argument
#print(myset1)

myset2 = set("hello")  # Creating a set from a string (order is arbitrary due to set being unordered)
#print(myset2)

myset3 = set()
myset3.add(1)
myset3.add(2)
myset3.add(2)
#print(myset3)

myset3.remove(2)  # Removing an element from the set
#print(myset3)

#for x in myset3:
#    print(x)

#if 1 in myset3:
#    print("Yes")

# Set operations in mathematics
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

u = odd.union(even)  # Union of two sets
#print("Union is:")
#print(u)

i = odd.intersection(prime)  # Intersection of two sets
#print("Intersection is:")
#print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}

diff = setA.difference(setB)  # Difference between two sets (elements in setA but not in setB)
#print("Difference is:")
#print(diff)

diff = setA.symmetric_difference(setB)  # Symmetric difference (elements in either set but not in both)
#print(diff)

setA.update(setB)  # Adding elements of setB to setA
#print(setA)

setA.intersection_update(setB)  # Updating setA with the intersection of setA and setB
#print(setA)

setA.difference_update(setB)  # Removing common elements between setA and setB from setA
#print(setA)

setA.symmetric_difference_update(setB)  # Updating setA with the symmetric difference of setA and setB
#print(setA)

setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}

#print(setD.issubset(setC))  # Checking if setD is a subset of setC
#print(setC.issuperset(setD))  # Checking if setC is a superset of setD

setE = {7, 8}
#print(setC.isdisjoint(setE))  # Checking if setC and setE have no common elements (disjoint sets)

# Applications of Sets in Machine Learning:
# - Data Preprocessing: Removing duplicates from a dataset
# - Feature Engineering: Using sets to represent categorical variables
# - Simulating user preferences in a recommender system
# - Evaluation Metrics: Calculating precision and recall using sets
# - Clustering: Using sets to represent clusters of data points
# - Graphs and Networks: Using sets to represent nodes and edges in a graph

# Additional Examples:
data = [1, 2, 3, 4, 1, 2, 5]
unique_data = set(data)
#print(unique_data)  # Output: {1, 2, 3, 4, 5}

dataset = ["apple", "banana", "orange", "apple", "kiwi"]
unique_words = set(dataset)
#print(unique_words)  # Output: {'banana', 'orange', 'kiwi', 'apple'}

document = "This is a sample document for demonstration purposes"
document_words = set(document.split())
#print(document_words)  # Output: {'This', 'sample', 'a', 'document', 'is', 'for', 'purposes', 'demonstration'}

user_preferences = {'action', 'comedy', 'drama'}  # Simulating user preferences for movie genres

actual_classes = {'cat', 'dog', 'rabbit'}
predicted_classes = {'dog', 'rabbit', 'hamster'}

true_positives = actual_classes.intersection(predicted_classes)
precision = len(true_positives) / len(predicted_classes)
recall = len(true_positives) / len(actual_classes)

#print("Precision:", precision)
#print("Recall:", recall)

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D'},
    'C': {'A', 'E'},
    'D': {'B'},
    'E': {'C'}
}

cluster1 = {1, 2, 3}
cluster2 = {4, 5, 6}
cluster3 = {7, 8, 9}
# Each cluster contains a set of data points sharing similar characteristics

