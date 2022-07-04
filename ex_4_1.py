a = input('Введите знак(*,/,+,-): ')
b = float(input('Введите первое число: '))
c = float(input('Введите второе число: '))
while exit != 'да':
    if a == '/' and c != 0:
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
    if a == '/' and c == 0:
        print('На ноль делить нельзя!')
    exit = input('Вы хотите закончить?(да/нет): ')
    if exit == 'да':
        print('калькулятор завершил свою работу')
        break
    a = input('Введите знак(*,/,+,-): ')
    b = float(input('Введите первое число: '))
    c = float(input('Введите второе число: '))
    
