list_full = []
for i in range(301):
    list_full.append(i)
print(list_full)

for i in list_full:
    if i % 2 == 0:
        print(i)
    if i == 297:
        break
