a = int(input("Введите год рождения: "))
b = int(input("Введите номер месяца рождения: "))
c = int(input("Введите год сегодняшнего дня: "))
d = int(input("Введите месяц сегодняшнего дня: "))
if d - b < 0:
    print(c - a - 1)
else:
    print(c - a)
