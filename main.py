# Seminar1
# Задача №1. Решение в группах
# За день машина проезжает п километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:2
# print(type(n)) определяет тип 
# 1 вариант решения
# n = int(input ("Расстояние в день"))
# m = 750

# res = bool(m%n) + ( m// n)
# print(res)

# 2Правильный вариант решения
# n = 750
# m = 700
# res = (m + n - 1) //n
# print(res)
# 3 вариант решения
# n = 700
# m = 750
# res = -(-m // n)
# print(res)
#  Задача 2
# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
# которое нужно приобрести для них. Input: 20 21 22(ввод чисел НЕ в одну строку) 
# Output: 32
# 1 вариант
# n = int(input("Количество учащихся в 1 классе:"))
# m = int(input("Количество учащихся во 2 классе:"))
# v = int(input("Количество учащихся в 3 классе:"))
# res = -(-n // 2 + -m // 2 + - v // 2)
# print(res)
# 2 вариант эталон решения
# n = int(input("Количество учащихся в 1 классе:"))
# m = int(input("Количество учащихся во 2 классе:"))
# v = int(input("Количество учащихся в 3 классе:"))
# res = ((n + 1)//2 + (m + 1) //2 + (v + 1) // 2)
# print(res)
# 3 вариант
# res = (a//2)+(b//2)+(c//2)+(a%2)+(b%2)+(c%2)
# 4 вариант
# print(f"Нужно {math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)} парт")
# math.ceil- округление до ближайшего большего числа
# Задача 3
# Дано натуральное число. Требуется определить, является ли год с данным номером
# високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним,
# что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400. 
# Input: 2016 Output: YES
# 1 вариант
# a = int(input('Введите год:'))

# if ((a % 4 == 0) and (a % 100 != 0))  or (a % 400 == 0):
#     print("yes")
# else:
#     print("no")
# 2 вариант
# year = int(input("Введите год:"))

# if (year % 400 ==0):
#     print("Yes")
# elif (year % 4 == 0 and year % 100 != 0):
#     print("yes")
# else:
#     print("no")
# 3 вариант решения
# y = int(input("Введите год:"))
# res = 'Yes' if ((y%4==0) and (y%100!=0)) or (y%400==0) else'No'
# print(res)
