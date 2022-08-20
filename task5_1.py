with open('file.txt', 'a+', encoding='utf-8') as f:
    while True:
        user_data = input('Введите данные. Для окончания записи нажмите Enter, без ввода данных:\n')
        if not user_data:
            break
        f.write(f'{user_data}\n')
    f.seek(0)
    print(f'Данные пользователя:\n{f.read()}')
