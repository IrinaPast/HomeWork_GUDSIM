def my_sum():
   res = 0
while True:
    li = input("Введите числа через пробел, для выхода - stop: ").split()
    for num in li:
        if num == "stop":
            return res
    else:
        try:
            res += res + int(num)
        except ValueError:
         print("Для выхода - stop")
    print("Сумма = ", res)