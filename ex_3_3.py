a=0
b=0
numbers = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]

for i in numbers:
    if i%2==0:
        a += 1

for i in numbers:
    if i%2 != 0:
        b +=1

print('четные числа:', a, 'нечетные:', b)


