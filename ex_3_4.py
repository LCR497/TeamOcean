numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
num = []
b = 0
for i in numbers:
    if numbers[b] >= 1:
        num.append(1)
    elif numbers[b] <= -1:
        num.append(-1)
    elif numbers[b] == 0:
        num.append(0)
    b += 1
print(num)