# Калькулятор

def calculator (change):
    if change not in [1,2,3,4,5,6,7]:
        return 'Конец вычислений'
    a = float(input('Введите а '))
    b = float(input('Введите б '))
    if change == 1:
        return a+b
    if change == 2:
        return a-b
    if change == 3:
        return a*b
    if change == 4:
        return a/b
    if change == 5:
        return a%b
    if change == 6:
        return a//b
    if change == 7:
        return a**b
        
    
change = None
while change in [1,2,3,4,5,6,7] or change == None:
    print('Операции: 1. Сложение 2. Вычитание 3. Умножение 4. Деление','\n',
    '5. Остаток от деления 6. Целочисленное деление 7. Возведение в степень', sep='')
    change = float(input('Введите номер операции '))
    print(calculator(change))