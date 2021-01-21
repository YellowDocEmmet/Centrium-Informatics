a = 0
b = 7851
for i in range(1305, 7851):
    if i % 4 == 0 or i % 7 == 0 and i % 11 != 0 and i % 17 != 0 and i % 19 != 0 and i % 21 != 0:
        a += 1
        if b > i:
            b = i
print(a, b)
