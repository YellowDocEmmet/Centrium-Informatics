a = float(input("Введите массу первого тела:"))
b = float(input("Введите объём первого тела:"))
m = float(input("Введите массу второго тела:"))
v = float(input("Введите объём второго тела:"))
if a / b > m / v:
    print("Плотность первого тела больше")
elif a / b < m / v:
    print("Плотность второго тела больше")
else:
    print("Плотности тел равны")
