import random


def random_number_generator(num):
    start = 0

    while start < num:
        yield random.randint(0, 100)
        start += 1


# for i in random_number_generator(10):
#     print(i)

iterator = iter(random_number_generator(4))
print(next(iterator)) # start = 0
print(next(iterator)) # start = 1
print(next(iterator)) # start = 2
print(next(iterator)) # start = 3
# print(next(iterator)) # start = 4, 4 < 4 == False

print([x for x in range(10)])

list_of_values = []

for i in range(10):
    list_of_values.append(i)


for i in (i for i in range(100)):
    print(i)

