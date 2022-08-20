with open('file3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor},\nСредний оклад {sum(map(float, sal)) / len(sal)}')
