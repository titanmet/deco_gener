from functools import reduce

d = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(d)