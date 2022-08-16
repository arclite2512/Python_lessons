from itertools import count

print("Итератор, генерирующий целые числа, начиная с указанного:")
for item in count(1):
    if item > 10:
        break
    else:
        print(item)
#  ---------------------------------------------------------------------
    from itertools import cycle

my_list = [True, 'ABC', 123, None]
i = 0
for el in cycle(my_list):
    if i > 10:
        break
    print(el)
    i += 1
