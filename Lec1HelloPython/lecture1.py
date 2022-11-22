# print('hello world')

value = None
# print(type(value))

a = 450
b = 1.23
s = 'hello world'
# value = "24342"  # str
# print(a)  # int
# print(b)  # float
# print(type(a))
# print(type(b))
# print(type(value))
# print(s)  # вывод строки

# phrase = 'можно использовать и двойные(") и одинарные кавычки(\'), и исп. их вместе'
# print(phrase)
# # через запятую указываем переменные и текст в кавычках:
# print(a, ' - ', b, ' - ', s)
# # формат #450  -  1.23  -  hello world:
# print('{}  -  {}  -  {}'.format(a, b, s))
# # меняем порядок #hello world  -  450  -  1.23:
# print('{2}  -  {0}  -  {1}'.format(a, b, s))
# print(f'{a} - {b} - {s}')  # интерполяция

# f = True
# print(f)
# print(type(f))

# listNum = [1, 2, 3]
# listStr = ['1', 'hi there']
# print(listNum)
# print(type(listNum))
# print(listStr)

# prit(a, ' + ', b, ' = ', a + b)

# print('Введите число c')
# c = int(input())  # принудительно указываем нужный формат
# print('Введите число d')
# d = int(input())
# print(type(c))
# print(c, ' + ', d, ' = ', c + d)  # здесь при 2 и 900 получаем уже 902

# a = 2
# b = 8
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# g = a // b
# h = a % b
# i = a ** b
# print(i)

# a = 4.2
# b = 3
# # c = a * b #12.600000000000001
# c = round(a * b, 2) #12.6
# print(c)

# a = 3
# a = a + 5 #то же что и
# print(a)
# b = 3
# b += 5 #это
# print(b)
# c = 4
# c *= 3
# print(c)

# a = 1 > 3  # false
# print(a)
# b = 1 != 2
# print(b)  # true
# c = 1 < 3 < 5  # тройные и четверные неравеснтва тоже ок
# print(c)

# f = 1 > 2 or 4 < 6  # true - дизъюнкция: хбо высказывание истина
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)  # true
# print(not 2 in f)  # false

# # is_odd = f[0] % 2 == 0 #одно и то же
# is_odd = not f[0] % 2  # одно и то же
# print(is_odd)


# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# num = int(input('number = '))
# if num > 1000:
#     print("it's big number")
# elif 100 < num <= 1000:
#     print("it's not so big number")
# elif 0 <= num <= 100:
#     print("it's small number")
# else:
#     print("it's number under 0")

# original = 2356
# inverted = 0
# print(type(inverted))
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)
# print(type(inverted))
# # к while можно добавить также else

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# r = range(6)
# for i in r:
#     print(i)

# for i in range(3, 6):  # 3 4 5
#     print(i)

# for i in range(1, 10, 2):  # 1 3 5 7 9
#     print(i)

# for i in ('qwe - try'):  # вывод по каждой букве на нвоой строке
#     print(i)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# # for c in text:
# # print(c)

# # срезы
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# # по умолч:(text[0:len(text)-1]) (==print(text)) съешь ещё этих мягких французских булок:
# print(text[:])
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# print(text=text[2:9] + text[-5] + text[:2])  # ешь ещёбсъ


# # Списки:
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue
# for e in colors:
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')
# del colors[1]  # удалить элемент

# # Функции
# def f(x):
#     return x**2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1
print(f(arg))
print(type(f(arg)))
