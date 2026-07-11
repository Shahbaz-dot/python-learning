def count():
    yield 1
    yield 2

for i in count():
    print(i)