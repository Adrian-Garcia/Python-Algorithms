"""
a[start:stop]		items start through stop-1
a[start:]			items start through the rest of the array
a[:stop]			items from the beginning through stop-1
a[:]				a copy of the whole array
"""

a = [0, 1, 2, 3, 4, 5]


print(a[0:4])  # [0, 1, 2, 3]

# Intems from index one to index 3-1
print(a[1:3])  # [1, 2]

# All items from index 1 to end
print(a[1:])  # [1, 2, 3, 4, 5]

# All items from the start to index 3-1
print(a[:3])  # [0, 1, 2]

# Copy of array
print(a[:])  # [0, 1, 2, 3, 4, 5]

# Last item in array
print(a[-1])  # 5
