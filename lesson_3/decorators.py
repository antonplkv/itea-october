from functools import wraps

def decorator(number=3):

    def actual_decorator(func):

        @wraps(func)
        def wrapper(name):
            print('-' * number)
            result = func(name)
            print('-' * number)
            return 1
        return wrapper

    return actual_decorator


@decorator(18)
def target_function(name):
    print(f'Hello world, {name}')
    return 'Hello world'


@decorator(30)
def target_function2(name):
    print(f'Hello world, {name}')
    return 'Hello world'


# print(target_function.__wrapped__('Anton'))
# result = target_function('Anton')
# result2 = target_function2('Anton')
# print(result)


decorator(10)(target_function2.__wrapped__)('Anton')


