"""
Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
n = int(input("Введите количество элементов в массиве: "))
list = [int(input()) for item in range(n)]
print(list)
c = int(input("Введите число: "))
min = abs(c - list[0])
index = 0
for i in range(1, n):
        count = abs(c - list[i])
        if count < min:
            min = count
            index = i

  
print("Числo", list[index] , "в массиве наиболее близко по величине к числу", c)

