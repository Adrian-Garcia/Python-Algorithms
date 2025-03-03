from typing import OrderedDict

dict = dict()

dict["a"] = 1
dict["b"] = 2
dict["c"] = 3
dict["d"] = 4
dict["e"] = 5
dict["f"] = 6
dict["g"] = 7
dict["h"] = 8
dict["i"] = 9

print("\ndict: {")
for key, element in dict.items():
    print(f"    {key}: {element}")

orderedDict = OrderedDict()

orderedDict["a"] = 1
orderedDict["b"] = 2
orderedDict["c"] = 3
orderedDict["d"] = 4
orderedDict["e"] = 5
orderedDict["f"] = 6
orderedDict["g"] = 7
orderedDict["h"] = 8
orderedDict["i"] = 9

print("}\n\norderedDict: {")
for key, element in orderedDict.items():
    print(f"    {key}: {element}")
print("}")
