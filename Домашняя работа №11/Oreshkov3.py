a = 0
b = 0
for i in range(1100, 11001):
    if i % 6 == 0 and i % 7 != 0 and i % 17 != 0 and i % 13 != 0 and i % 23 != 0:
        a += 1
        if b < i:
            b = i
print(a, b)
