# cars = ['BMW', 'Mercedes', 'Volkswagen']
# print(cars.count('BMW'))
# print(cars)
# cars[0] = 'Audi'
# print(cars)
# cars.append('Lamborghini')
# print(cars)
#
# cars.append(['Porsche', 'Renault', 'Chevrolet'])
# print(cars)
# print(cars[4][2])
#
# list_1 = ['1', '2', '3']
# list_2 = ['4', '5', '6']
# list_3 = list_1 + list_2
# print(list_3)


products = {
    ('banana', 'FruitsAAA'): 5,
    'orange': 9,

}

updated_products = {'carrot': 10, 'milk': 2, 'orange': 10}
products.update(updated_products)
print(products)


num_of_bananas = products[('banana', 'FruitsAAA')]
num_of_oranges = products['orange']
num_of_potato = products.get('potato')

products['tomato'] = 15

print(products)

print(num_of_bananas, num_of_oranges, num_of_potato)

cars = {
    'Mercedes': {
        'g63': 3333,
        'e500': 9999
    }
}

my_set = {'1', '2', '3', '4', '5', '1', '2', '5', '6'}
print(my_set)

products_set_1 = {'fish', 'meat', 'carrot'}
products_set_2 = {'chicken', 'fish', 'carrot'}
diff = products_set_2 - products_set_1
print(diff)
intersect = products_set_1 & products_set_2
print(intersect)
sum([1, 2, 3])
sum_ = products_set_1 | products_set_2
print(sum_)
sum([1, 2, 3])

