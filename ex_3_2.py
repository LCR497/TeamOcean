k = 0
first = []
second = []
third = []
while True:
    user = input('Введите предложение: ')
    user = user.split(' ')
    if len(user) >= 6:
        k = len(user) / 2
        d = int(len(user))
        if int(len(user)) % 2 == 0:
            for i in user[:int(k)]:
                first.append(i)
            for j in user[int(k)::]:
                second.append(j)
            for i in second:
                third.append(i)
            for i in first:
                third.append(i)
            print(third)
            break
        else:
            for i in user[:int(k)]:
                first.append(i)
            for j in user[int(k)::]:
                second.append(j)
            for i in second:
                third.append(i)
            for i in first:
                third.append(i)
            print(third)

    else:
        print('Error')

