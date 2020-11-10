even_numbers = [2, 4, 6, 8]

metaclass = type(type(even_numbers))
print(type(metaclass))


def get_num_of_wheels(self):
    return self.NUM_OF_WHEELS


Vehicle = type('Vehicle123', (), {'NUM_OF_WHEELS': 4, 'get_num_of_wheels': lambda self: self.NUM_OF_WHEELS})

print(Vehicle)
print(Vehicle.NUM_OF_WHEELS)
print(Vehicle().get_num_of_wheels())


class DriveMixin:

    def drive(self):
        print(f'{self.model} is driving')


class CarMetaClass(type):

    def __new__(mcs, name, base, attrs):
        if not attrs.get('NUM_OF_WHEELS'):
            raise NotImplementedError('NUM_OF_WHEELS attribute is required')
        base = (DriveMixin, )
        car_class = super().__new__(mcs, name, base, attrs)
        return car_class


class Car(metaclass=CarMetaClass):

    NUM_OF_WHEELS = 4

    def __init__(self, engine, model):
        self.engine = engine
        self.model = model

    def __call__(self, *args, **kwargs):
        print(f'I am {self.model}')


car = Car('V-8', 'mercedes')
car()

import time


class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time() - start
        return result, end


@Decorator
def do_nothing(seconds):
    time.sleep(seconds)


print(do_nothing(2))