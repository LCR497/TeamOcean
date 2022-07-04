sequence_0 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0)
sequence_1 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, '70')
sequence_2 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70', 0.0)
sequence_3 = (14, 10, 35, 45, '60', 70, 90, 0, 105, 150, 10.0, 45.0, '70')
unique = []
unique1 = []
unique2 = []
unique3 = []
a = 0
for i in sequence_0:
    if i in unique:
        print(i)
        a += 1
    else:
        unique.append(i)
if a == 0:
    print('В 1 последовательность уникальна')
else:
    print('В 1 последовательность неуникальна')
b = 0
for j in sequence_1:
    if j in unique1:
        print(j)
        b += 1
    else:
        unique1.append(j)
if b == 0:
    print('Во 2 последовательность уникальна')
else:
    print('Во 2 последовательность неуникальна')

c = 0
for k in sequence_2:
    if k in unique2:
        print(k)
        c += 1
    else:
        unique2.append(k)
if c == 0:
    print('В 3 последовательность уникальна')
else:
    print('В 3 последовательность неуникальна')
d = 0
for l in sequence_3:
    if l in unique3:
        print(l)
        d += 1
    else:
        unique3.append(l)
if d == 0:
    print('В 4 последовательность уникальна')
else:
    print('В 4 последовательность неуникальна')