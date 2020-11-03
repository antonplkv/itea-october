def hello_world(name):
    return f'Hello world. My Name is {name}'

print(hello_world('Anton'))


hello_world_lambda = lambda n: f'Hello world. My name is {n}'

print(hello_world_lambda('Anton'))

hw = hello_world

hw('Anton')