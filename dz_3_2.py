# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

n=int(input('введите длину списка: '))

if n < 1:
    print('введено некорректное значение')
    quit()

list = []

for i in range(n):
    list.append(random.randint(1, 9))
    
print(list)

list2 =[]
m = int(n/2) # вывод только элементов, имеющих пару.

for i in range(1, m+1):
        list2.append(list[i-1]*list[-i])

if n%2 != 0: # при нечетном количестве элементов, элемен находящийся в середине списка, выводится без изменения (как в списке)
    list_tmp =[]
    list_tmp.append(list[m]) 
    list2.extend(list_tmp)
    
print(list2)