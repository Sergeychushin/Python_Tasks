# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
count = 1

while count < n:
    if n % 2 == 0:
        print(count)
        count = count * 2
    else: 
      n -= 1