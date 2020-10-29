
t_1 = '1'
t_2 = '0'


try:
    result = t_1 + t_2
except TypeError as e:
    error_text = str(e)
    print(e)
    result = 'Произошла ошибка типов'
except ArithmeticError as e:
    error_text = str(e)
    print(e)
    result = 'Прозиошла арифметическая ошибка'
else:
    print('Ура, у нас не было исключений')
finally:
    print('Работа блока try except завершена')

print(result)


def hate_ones(arg1, arg2):
    if 1 in (arg1, arg2):
        raise ValueError('Я отказываюсь работать с единицами!!!')

    return arg1 + arg2

hate_ones(1, 20)