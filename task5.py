my_list = [9,7,5,4,3,2,1]
n = int(input("Введите число: "))
i = 0
for el in my_list:    if n <= el:
        i = i+1
my_list.insert(i,n)
print(my_list)