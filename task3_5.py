def sum_num():
    s = 0
    while True:
        err = False
        in_list = input("Введите числа через пробел, нажмите  'q' для выхода: "). split()
        for num in in_list:
            if num.lower() == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    err = True
        if err:
            print("Данные введены неправильно!")
        print(f"Сумма чисел = {s}")


print(sum_num())
