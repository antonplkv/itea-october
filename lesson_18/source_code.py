import random

def number_randomize(quanity):

    if not isinstance(quanity, int):
        raise TypeError('Wrong type')

    numbers = [0, 2, 3, 4, 5, 6, 7, 8, 9, '1', '2', '3']

    for i in range(quanity):
        yield random.choice(numbers)

print(list(number_randomize(3)))

