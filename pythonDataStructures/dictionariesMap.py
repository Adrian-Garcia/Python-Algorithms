# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
myDict = { 			# Dictionary with values
	"Adrian" : "Garcia",
	"Fernanda" : "Manzanita"
}

newDict = {}		# Dictionary from scratch
newDict["Pokemon Name"] = "Tyranitar"
newDict["HP"] = 123

# Print dictioanry
print(myDict)
print(newDict)

# Search for value in dictionary
if "Fernanda" in myDict:
	print ("\nFernanda is on the dictionary, her last name is {}".format(myDict["Fernanda"]))

# Access to the value of dictionary from key
print (newDict["Pokemon Name"])

# Update value from key
myDict["Fernanda"] = "Martinez"
print(myDict, end='\n\n')

# For loop in dictionary
for i in myDict:
	print("{} : {}".format(i, myDict[i]))

# Delete from dict
newDict.pop("HP")
print()
print(newDict)

# Clear dictionary
newDict.clear()
print(newDict)

# Copy a dictionary
newDict = myDict.copy()
print("myDict = {}".format(myDict))
print("newDict = {}".format(newDict))

# Nested dicts
myfamily = {
	"child1" : {
		"name" : "Emil",
		"year" : 2004
	},
	"child2" : {
		"name" : "Tobias",
		"year" : 2007
	},
	"child3" : {
		"name" : "Linus",
		"year" : 2011
	}
}
print(myfamily)