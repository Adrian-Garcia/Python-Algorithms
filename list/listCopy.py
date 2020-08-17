listOriginal = [1,2,3]
listCopy = listOriginal

print(listOriginal)	# 1 2 3
print(listCopy)		# 1 2 3

listCopy.append(4)

print(listOriginal)	# 1 2 3 4
print(listCopy)		# 1 2 3 4
print()

listOriginal = [1,2,3]
listCopy = listOriginal.copy()

print(listOriginal)	# 1 2 3
print(listCopy)		# 1 2 3

listCopy.append(4)

print(listOriginal)	# 1 2 3
print(listCopy)		# 1 2 3 4