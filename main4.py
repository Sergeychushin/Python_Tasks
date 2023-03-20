"""""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""
# Var_1
my_str = 'a a a b c a a d c d d'
my_list = my_str.split()
dict = {}
print(my_list)

for i in my_list:
    if i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end = ' ')
    else:
        dict[i] = 0
        print(i, end = " ")
print()

#var_2   
print('Этот вариант, если нужно split применить обязательно')

my_list = my_str.split()
print(my_list)
for i in range(len(my_list)):
  if my_list.count(my_list[(i + 1) * -1]) > 1:
    my_list[(i + 1) * -1] += f'_{str(my_list.count(my_list[(i + 1) * -1]) - 1)}'

print(my_list)


# Var_3 Этот вариант больше похож на пример в задании
print('Этот вариант больше похож на пример в задании')

print(my_str)
new_str = ''

for i in range(len(my_str)):
  if my_str[i] != ' ' and my_str.count(my_str[i], 0, i) > 0:
    new_str += f'{my_str[i]}_{my_str.count(my_str[i], 0, i)}'
  else: 
    new_str += my_str[i]

"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается 
последовательность непробельных символов идущих 
подряд, слова разделены одним или большим числом 
пробелов. Определите, сколько различных слов 
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
"""

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
print(text)
text_ = i.upper()
text_ = text_.replace('.', ' ').split()
set_text = set(text_)
print(f'{len(set_text)}')


""""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит 
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не 
такими смышлеными. Никто из ребят не смог до 
конца сделать это задание. Они решили так: у кого 
будет меньше ошибок в коде, тот и выиграл спор. За 
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих 
слайдах
"""""
n = int(input())
max_ = n

while n != 0:
   if n > max:
      max = n
   n = int(input())
print(f'{max_ = }')