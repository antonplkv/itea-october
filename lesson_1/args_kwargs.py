def sum_(required_value, *args):
    print(args)
    result = 0
    for i in (required_value, ) + args:
        result += i
    return result


data = []

result = sum_(1, 2)
print(result)
# То же, что и выше
sum_(100, 200, 300, 400)



def products_sum(**kwargs):
    print(kwargs)


products = {
    'tomato': 10,
    'orange': 20,
    'carrot': 3,
    'meat': 2
}

products_sum(**products)

# Тоже самое, что и Выше
products_sum(tomato=10, orange=20, carrot=3, meat=2)




data = [100, 200, 300, 400]

a = 10
b = 20

a, b = b, a

a1, a2, a3, a4 = data

print(a1, a2, a3, a4)





