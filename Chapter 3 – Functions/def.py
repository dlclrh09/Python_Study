def add(a, b):
    print("add")
    return a + b


x = 3
y = 5
z = add(x, y)
print(z)


def sub(a, b):
    print("sub")
    if a > b:
        return a + b
    else:
        return a - b


x = 1
y = 2
z = sub(x, y)
print(z)


def hello(name):
    print('hello' + name)

hello('alice')
hello('jone')
