a = 0
b = 0
for i in range(3201, 12877):
    if i % 4 == 0 and i % 11 != 0 and i % 13 != 0 and i % 7 != 0 and i % 19 != 0:
        a += 1
        if b < i:
            b = i
print(a, b)
