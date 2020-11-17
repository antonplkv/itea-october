class CustomArray:

    def __init__(self, size, type_):
        self._list = [0] * size
        self._type = type_

    def __getitem__(self, item):
        return self._list[item]

    def __setitem__(self, key, value):

        if isinstance(key, int) and type(value) == self._type:
            self._list[key] = value
        else:
            raise TypeError('Type error')


for i in CustomArray(10, int):
    print(i)


numbers = [10, 20, 8, 300]

for i, v in enumerate(numbers):
    print(i, v)
