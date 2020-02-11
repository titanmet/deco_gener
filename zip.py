s = [1, 2]
v = ['a', 'b']

z = zip(s, v)
print(next(z))
print(next(z))

def my_zip(first, second):
    for i in range(len(first)):
        yield  first[i],second[i]

z = my_zip(s, v)
print(next(z))
print(next(z))