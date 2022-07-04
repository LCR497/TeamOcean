numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
k = 0
i = 0
j = 0
while k < len(numbers):
    if numbers[i] < numbers[j]:
        print(numbers[j])
    i = j
    j += 1
    k += 1
