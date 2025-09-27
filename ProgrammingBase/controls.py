# 1. Условный оператор if
# -----------------------------------
#
# Синтаксис:
# 
# a)
# if условие:
#     блок кода
#
# b)
# if условие:
#     блок кода
# else:
#     блок кода
#
# c)
# if условие_1:
#     блок кода_1
# elif условие_2:
#     блок кода_2
# ...
# else:
#     блок кода

# number = int(input())

# if number > 0 and number < 100 or \
#    number > 100 and number < 200 or \
#    number * number + 10 < 50:
#     print("positive")
#     print("positive again")

# if number > 0:
#     print("positive")
# else:
#     print("non positive")

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero")

day_of_week = input()

# if day_of_week == "Понедельник":
#     print(1)
# ...

match day_of_week:
    case "Понедельник" | "понедельник":
        print(1)
    case "Вторник" | "вторник":
        print(2)
    case "Среда" | "среда":
        print(3)
    case "Четверг" | "четверг":
        print(4)
    case "Пятница" | "пятница":
        print(5)
    case "Суббота" | "суббота":
        print(6)
    case "Воскресенье" | "воскресенье":
        print(7)
    case _:
        print("Ожидается название дня недели")
