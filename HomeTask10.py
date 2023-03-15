# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input("Введите количество монет: "))
count = 0
o_coin = 0
r_coin =0

for i in range(n):
    coin = int(input("Укажите положение монеты (0 - герб / 1 - решка): "))
    if coin == 0:
        o_coin += 1
    elif coin != 0:
        r_coin += 1
        
if o_coin > r_coin:
    print(r_coin, "- количество монет, которые необходимо перевернуть.")
else:
    print(o_coin, "- количество монет, которые необходимо перевернуть.")


