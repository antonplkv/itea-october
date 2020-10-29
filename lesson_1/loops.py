
# i = 0
# while True:
#     print(i)
#     i += 1

list_of_numbers = list(range(0, 100))

# i = 0
# len_of_list = len(list_of_numbers)
#
# while i < len_of_list:
#     print(list_of_numbers[i])
#     i += 1

my_dictionary = {
    1: 2,
    5: 10,
    10: 20
}

for k, v in my_dictionary.items():
    if k == 5:
        continue
    print(k, v)