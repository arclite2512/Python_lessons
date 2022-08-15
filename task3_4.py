def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Введите вещественное число и целое отрицательное число"
    return res


print(my_func(3.2, -4))

# ----------------------------------------------------------------------------------------------------------------------

def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Неправильно введены данные: \nx должен быть больше 0\ny должен быть меньше 0"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            print("Результат возведения х в степень у:")
            return round(result, 6)
    except ValueError:
        return "программа работает только с числами."


number1 = input('Введите действительное целое число, х = ')
number2 = input('Введите целое отрицательное число, у = ')

print(my_func2(number1, number2))
