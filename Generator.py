# import sys

# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(sys.getsizeof([]))
# print(sys.getsizeof([1]))
# print(sys.getsizeof([1, 2, 3]))
# print(sys.getsizeof(s))
# print(sys.getsizeof(list(range(0,10000000000000000000000000))))

def get_numbers():
    start = 0
    end = 10
    step = 1
    while start < end:
        yield start
        start += step

gen = get_numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(list(gen))
try:
    gen = get_numbers()
    for i in gen:
        print(i)
except StopIteration as e:
    print(e)
