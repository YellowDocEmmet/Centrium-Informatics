a = 0
b = 0
for i in range(1012, 9639):
    if i % 3 == 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        a += 1
        if b < i:
            b = i
print(a, b)

