# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
emptySet = set()
mySet = {"Fer", "Adrian", "Atenea", "Zeus"}
otherSet = {"Burbuja", "Lola"}

print(mySet)  # Print all elements in set

# For loop in a set
for i in mySet:
    print(i)

# Look for a value in set
if "Fer" in mySet:
    print("Fer was found")
else:
    print("Fer was not found")

# Add an element in the set
mySet.add("Hestia")
print(mySet)

# Remove an element in the set
mySet.remove("Hestia")
print(mySet)

# Discard an element in set (If the element is not in the set, nothing will happen)
mySet.discard("Hestia")
print(mySet)

# Delete last element in set
mySet.pop()
print(mySet)

# Join 2 sets
newSet = mySet.union(otherSet)
print(newSet)

# Clear set
newSet.clear()
print(newSet)
