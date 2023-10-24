number = int(input("Введите число для таблицы умножения: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")
