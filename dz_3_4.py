# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n=int(input('введите длину списка: '))
min = ''
max = ''
list = []
for i in range(n):
    list.append(round(random.uniform(1, 10), 2))
    
print(list)

list2 = []
for i in range(n):
    list2.append(round((list[i]%1), 2))
        
print(list2)

max = 0
min = list2[0]

for i in range(0, len(list2)):
    if list2[i] < min:
        min = list2[i]
    if list2[i] > max:
        max = list2[i]


print(f'наименьшее значение: {min}')
print(f'наибольшее значение: {max}')

print(f'разница между наибольшим и наименьшим значениями: {round((max - min), 2)}')