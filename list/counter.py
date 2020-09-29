import collections

print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print (collections.Counter({'a':2, 'b':3, 'c':1}))
print (collections.Counter(a=2, b=3, c=1))

# All returns Counter({'b': 3, 'a': 2, 'c': 1})