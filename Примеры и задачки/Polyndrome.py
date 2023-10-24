def is_palindrome(phrase):
    cleaned_phrase = ''.join(filter(str.isalnum, phrase)).lower()
    return cleaned_phrase == cleaned_phrase[::-1]

phrase = input("Введите фразу: ")
print("Да" if is_palindrome(phrase) else "Нет")
#def is_palindrome(phrase):: Это объявление функции is_palindrome, 
# которая принимает один аргумент phrase, представляющий введенную фразу.
#
#cleaned_phrase = ''.join(filter(str.isalnum, phrase)).lower(): 
# В этой строке создается новая строка cleaned_phrase, в которой происходит удаление всех символов,
# которые не являются буквами и цифрами, с использованием функции filter. 
# Затем вся строка преобразуется в нижний регистр с помощью .lower().
#
#return cleaned_phrase == cleaned_phrase[::-1]: Здесь функция сравнивает cleaned_phrase с самой собой, 
# перевернутой с помощью [::-1]. 
# Если они идентичны, то функция возвращает True, иначе возвращает False.
#
#phrase = input("Введите фразу: "): Запрашивается ввод фразы у пользователя.
#
#print("Да" if is_palindrome(phrase) else "Нет"): В зависимости от результата is_palindrome, 
# программа выводит "Да" (если фраза является палиндромом) или "Нет" (если фраза не является палиндромом).
# Это делается с использованием условного выражения if-else.