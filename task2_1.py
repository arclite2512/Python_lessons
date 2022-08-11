my_list = [12, (3, + 5j), None, -77, [8, 6], 'True', range(7), True, (1, 3, 4), frozenset(), 9.5]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
