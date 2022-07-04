a = input('Введите знак(*,/,+,-): ')
b = float(input('Введите первое число: '))
c = float(input('Введите второе число: '))
while exit != 'да':
    if a == '/':
        d = b / c
        print(d)
    elif a == '*':
        d = b * c
        print(d)
    elif a == '+':
        d = b + c
        print(d)
    elif a == '-':
        d = b - c
        print(d)
    exit = input('Вы хотите закончить?(да/нет): ')
    if exit == 'да':
        print('калькулятор завершил свою работу')
        break
    a = input('Введите знак(*,/,+,-): ')
    b = float(input('Введите первое число: '))
    c = float(input('Введите второе число: '))
    