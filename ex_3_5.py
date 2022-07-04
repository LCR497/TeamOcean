my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
b = 0
for i in my_list:
    if b % 2 == 0:
        print(b, my_list[b])
    b += 1
