with open('file2.txt', 'r', encoding='utf-8') as f:
    lines = [line.rstrip() for line in f.readlines()]
    f.seek(0)
    words = f.read().split(' ')
    print(f'Количество строк: {len(lines)}')
    for num, line in enumerate(lines, 1):
        print(f'Количество слов в {num} строке: {len(line.split())}')
