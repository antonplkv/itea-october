import json

products = {'Onion': {
        'price': 12,
        'in_stock': 1000,
        'description': 'Лук'

    },
        'Tomato': {
        'price': 4,
        'in_stock': 10000,
        'description': 'Помидоры'

    }, 'Cucumber': {
        'price': 10,
        'in_stock': 500,
        'description': 'Огурцы'

    }}


# products_json = json.dumps(products)
# products = json.loads(products_json)
# print(products)
# print(type(products))

f = open('myjson.json', 'r')
# json.dump(products, f)
data = json.load(f)
print(data)
f.close()


