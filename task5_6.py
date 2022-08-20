my_dict = {}
with open("file6.txt", encoding="utf-8") as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(my_dict)
