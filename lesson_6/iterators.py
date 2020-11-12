a = [1, 2, 3, 4, 5]
import random

# iterable = iter(a)
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))


class MyRangeIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        raise StopIteration


class MyRange:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterable(self.start, self.end)


print(tuple(MyRange(10, 20)))


class RandomIter:

    def __init__(self, numbers):
        self.counter = 0
        self.number = numbers

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            value = random.randint(0, 9999)
            self.counter += 1
            return value
        raise StopIteration


for i in RandomIter(10):
    print(i)


