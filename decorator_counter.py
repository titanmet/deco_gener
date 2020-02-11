def decorator1(func):
    func.counter = 1
    def fake(value):
        print('Run:', func.counter)
        func.counter += 1
        return func(value)

    return fake



@decorator1
def my_str(value):
    return str(value)

# my_str = decorator1(my_str)
print(my_str(123))
print(my_str(123))
print(my_str(123))