"""""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""""
n1 = int(input("Введите количество элементов в первом списке: ")) # без
list_1 = [int(input()) for item in range(n1)]     # аналог -> list_1 = [i for i in range(int(input()))]

n2 = int(input("Введите количество элементов во втором списке: "))
list_2 = [int(input()) for item in range(n2)]

print(list_1)
print(list_2)
list_3 = list_1 + list_2            # list_3 = list_1.intersection(list_2)
for i in set(list_3):               # 
    if list_3.count(i) >1:          # list_3.sort()
        print(i, end =' ')          # # print(*list_3)

