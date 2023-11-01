# Задача 2: Поиск максимального числа
numbers = input("Введите числа, разделенные пробелами: ")
numbers_list = numbers.split()
max_number = float(numbers_list[0])

for number in numbers_list:
    if float(number) > max_number:
        max_number = float(number)

print("Максимальное число:", max_number)
