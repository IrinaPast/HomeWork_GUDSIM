list1 = input("Введите элементы списка через пробел:").split()
for i in range(1, len(list1), 2):
    list1[i-1], list1[i] = list1[i], list1[i-1]
print(list1)

list1 = input("Введите элементы списка через пробел:").split()
for i in range(1, len(list1), 2):
    list1.insert(i-1, list1.pop(i))
print(list1)

