'''
Syntax:

while <cond>:
    <body>
[else:
    <else_body>]
'''

## Пример 1
# number = int(input('Введите число (0 для завершения): '))
# while number != 0:
#     print(number * number)
#     number = int(input('Введите число (0 для завершения): '))
# 
# print('Спасибо, что используете наше ПО!')

# # Пример 2
# number = int(input('Введите число (0 для завершения): '))
# while number != 0:
#     if number % 2 == 0:
#         print('Для четных чисел не работает!')
#         number = int(input('Введите число (0 для завершения): '))
#         continue
#     print(number * number)
#     number = int(input('Введите число (0 для завершения): '))

# print('Спасибо, что используете наше ПО!')

# # Пример 3
# number = int(input('Введите число (0 для завершения): '))
# while number != 0:
#     print(number * number)
#     number = int(input('Введите число (0 для завершения): '))
#     if number > 1000_000:
#         print('Вы ввели слишком большое число!')
#         break

# Пример 4
number = int(input('Введите число (0 для завершения): '))
while number != 0:
    print(number * number)
    number = int(input('Введите число (0 для завершения): '))
    if number > 1000_000:
        print('Вы ввели слишком большое число!')
        break
else:
    print('Все данные обработаны корректно!')


print('Спасибо, что используете наше ПО!')