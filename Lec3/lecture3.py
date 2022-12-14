# def f(x):
#     return x ** 2
#
#
# print(type(f))
#
# g = f  # Переменная хранит в себе ссылку на функцию
# print(f(2))
# print(g(2))
#
# -------------
# def calc1(x):
#     return x + 10
#
#
# print(calc1(10))
#
#
# def calc2(x):
#     return x * 10
#
#
# print(calc2(10))
#
#
# def math(op, x):
#     print(op(x))
#
#
# math(calc2, 15)
# math(calc1, 25)
# -------------

# def sum1(x, y):
#     return x + y
#
#
# # def mult1(x, y):
# #     return x * y
#
# mult1 = lambda x, y: x * y
#
#
# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
#
#
# calc(mult1, 4, 5)
# calc(lambda x, y: x * y, 4, 5)
# -------------

# list_1 = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list_1.append(i)
#
# print(list_1)
#
# list_2 = [i for i in range(1, 21)]
# print(list_2)
#
# list_3 = [i for i in range(1, 21) if i % 2 == 0]
# print(list_3)
#
# # кортежи
# list_4 = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list_4)
#
#
# # число и его куб
# def f(x):
#     return x ** 3
#
#
# list_5 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list_5)
# -------------
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# my_list = [(i, i ** 2) for i in list_1 if i % 2 == 0]
# print(my_list)


# ----не работает код ниже, разобраться, почему-----------

# path = 'numbers.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# list_1 = []
#
# # Пока моя строка не пустая:
# while data != '':
#     space_pos = data.index(' ')
#     list_1.append(int(data[:space_pos]))
#     data = data[space_pos + 1]
#
# for line in data:
#     list_1.append(line)
#
# my_list = [(i, i ** 2) for i in list_1 if i % 2 == 0]
# print(my_list)

# -------------улучшаем ф-ю:

# принимает первым аргументом функцию
# def select(f, coll):
#     return [f(x) for x in coll]
#
# 1ым аргументом принимает условие, по кот. нужно б. произвести фильтрацию о-та
# def where(f, coll):
#     return [x for x in coll if f(x)]
#
#
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# -------------
#  map() нам заменит нашу ф-ю select
# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# -------------
# data = list(map(int, input().split()))
# print(data)
#
# data = map(int, '1 2 3 54 67 88 100'.split())
# for e in data:
#     print(e)

# -------------

# data = [x for x in range(10)]
#
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# -------------Ещё больше улучшаем код:
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)
# -------------
users = ['user1', 'user2', 'user3']
ids = [4, 5, 9]
salary = [111, 222]

data = list(zip(users, ids))
print(data)

data = list(zip(users, ids, salary))
print(data)

data = list(enumerate(users))
print(data)
