    # Массивы/Списки в python
import random
    # Нахождение минимального/максимального элемента в списке
list1 = [2,4,5,6,7,8,9,100,-10]
min = 0
max = 0
for elem in list1:
    if min > elem:
        min = elem
    if max < elem:
        max = elem
print(f'Максимальное число {max}, минимальное число {min}')
print('Максимальное число {}, минимальное число {}'.format(max,min))
    # Создание рандомного списка
list2 = list()
for i in range(0,random.randint(1,10)):
    list2.append(random.randrange(0,100))
print(list2)

