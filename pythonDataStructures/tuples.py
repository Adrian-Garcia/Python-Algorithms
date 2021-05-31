# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
myTuple = ("Fer", "Adrian", "Atenea", "Zeus")

print(myTuple)  # Display the whole tuple
print(myTuple[0])  # Dipplay first element on tuple
print(myTuple[-1])  # Display last element on tuple
print(myTuple[1:4])  # Display from second to last element on tuple

myList = list(myTuple)  # Convert tuple to list

for i in myTuple:  # For loop on a tuple
    print(i)

# Search in tuple
if "Hestia" in myTuple:
    print("Hestia in tuple")
else:
    print("Hestia is not in tuple")
