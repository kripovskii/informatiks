# Задача 3: Подсчет гласных букв
input_string = input("Введите строку: ")
vowels = "aeiou"
count = 0

for char in input_string:
    if char.lower() in vowels:
        count += 1

print("Количество гласных букв:", count)
