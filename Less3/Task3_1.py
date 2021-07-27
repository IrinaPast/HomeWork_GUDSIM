def my_func():
    try:
        arg1 = float(input("введите число 1: "))
        arg2 = float(input('введите число 2: '))
        arg3 = arg1 / arg2
        return arg3
    except ZeroDivisionError:
            print("нельзя делить на ноль!")
a = my_func()
print(f"Результат деления: {a}")
