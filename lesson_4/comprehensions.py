
my_list = []

for i in range(10):
    my_list.append(i)
print(my_list)



print(my_list)
result_list = []

my_list = [i ** 2 if i > 3 else i for i in range(10) if i > 1]
for i in range(10):
    if i > 1:
        if i > 3:
            result_list.append(i ** 2)
        else:
            result_list.append(i)
print(result_list)

result = {i: i ** 2 for i in range(10)}
print(result)