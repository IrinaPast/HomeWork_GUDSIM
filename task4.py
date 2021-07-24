s = input('введите данные через пробел:').split()
for i, el in enumerate(s):
    print(i, el[:10])