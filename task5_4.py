num_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
}

with open('file4.txt', 'r', encoding='utf-8') as f:
    rus_nums = []
    for line in f.readlines():
        new_line = line.split()
        new_line[0] = num_dict[new_line[0].lower()]
        rus_nums.append(f'{new_line[0].capitalize()} {new_line[1]} {new_line[2]}\n')
    with open('file4_2.txt', 'w', encoding='utf-8') as f2:
        f2.writelines(rus_nums)
        