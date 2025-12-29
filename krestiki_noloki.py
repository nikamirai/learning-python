# Программа крестики нолики. Каждый квадрат имеет свое число от 1 до 9

print('Схематическое представление нашей таблицы')
print('-----')
print('1|2|3')
print('_____')
print('4|5|6')
print('_____')
print('7|8|9')
print('-----')

point_a = [] # здесь будут храниться все клетки игрока а
point_b = [] # здесь будут храниться все клетки игрока б
kol_change = 0 # сколько раз игроки выбирали клетку

# Игрок выиграл если:
# он набрал комбинацию 1,5,9 или 3,5,7 или 2,5,8 или 4,5,6
valid_point = [[1,5,9], [3,5,7], [2,5,8], [4,5,6]]

while ((point_a not in valid_point) and (point_b not in valid_point)) and kol_change!=9:   
    if kol_change % 2 == 0 or kol_change == 0:
        num_kletki = int(input('Игрок а введите номер клетки '))
        # клетка уже занята или нет
        while (num_kletki in point_b) or (num_kletki in point_a):
            num_kletki = int(input('Введите не занятую клетку'))
        point_a.append(num_kletki)
        kol_change += 1
    else:
        num_kletki = int(input('Игрок б введите номер клетки '))
        # клетка уже занята или нет
        while (num_kletki in point_b) or (num_kletki in point_a):
            num_kletki = int(input('Введите не занятую клетку '))
        point_b.append(num_kletki)
        kol_change += 1

if point_a in valid_point:
    print('Поздравляем игрока А')

if point_b in valid_point:
    print('Поздравляем игрока Б')



