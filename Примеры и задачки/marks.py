def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    return total / count

num_subjects = int(input("Введите количество предметов: "))
grades = []

for i in range(num_subjects):
    grade = float(input(f"Введите оценку за предмет {i + 1}: "))
    grades.append(grade)

average = calculate_average(grades)
print(f"Средний балл ученика: {average}")
