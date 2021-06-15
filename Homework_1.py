# #task1#
# a = input("Enter a:")
# a = int(a)
# b = 5
# c = b ** a
# int(c)
# print("5 в степени a = ",c)
#
# #task2#
# a = input("Enter the time in seconds:")
# a = int(a)
# h = a // 3600
# b = a % 3600
# m = b // 60
# s = a % 60
# print(h,"h:",m,"m:",s,"s")
#
#
# #task3#
# a = (input("Print the namber: "))
# b = int(a*2)
# c = int(a*3)
# a = int(a)
# d = int(a + b + c)
# print(a,"+",b,"+",c, "=", d)

#task4

#a = int(input("Введите целое положительное число: "))
#b = a % 10
#a = a // 10
#while a > 0:
#    if a % 10 > b:
#        b = a % 10
#   a = a // 10
#print("Наибольшее число: ", b )


#task5
a = int(input("Введите прибыль: "))
b = int(input("Введите издержки: "))
if a - b > 0:
    c = a - b
    print("выручка больше издержек")
    r = c/a
elif a - b < 0:
    print("издержки больше выручки")
d = int(input("введите количество сотрудников: "))
e = c / d
print("прибыль в расчете на одного сотрудника: ", e)

