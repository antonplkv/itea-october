from typing import Tuple, List, Union


# def is_upper(string: str, age: int):
#     print(age * 1)
#     return string.isupper()
#
# is_upper('qweqweqw', 123)
# is_upper(312312, '1231')


def calculate_cart(cart_tuple: List[str, int]):
    """('Banana', 35, 'Tomato', 45)"""
    pass


calculate_cart(['Banana', 35, 'Tomato',  45, 'Strawberry', 7])


class A:

    def get(self):
        return 'A'


def work_with_a(obj: A = A()):
    obj.get()


def test_func(arg1: Union[int, str, tuple]):
    pass


test_func((1, 2))


def test_cart(products: Tuple[Union[str, int], float]):
    pass


test_cart(('weqwe', 1))


def q(arg1, arg2):
    """
    Adds multiple values

    :param arg1: int
    :param arg2: str
    :return: int
    """
    return arg1 + int(arg2)


q()