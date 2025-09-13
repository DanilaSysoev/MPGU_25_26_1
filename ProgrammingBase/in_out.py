# Output

print('Hello')
print('Привет')
print(123)
print(1, 2, 3)

print('Hello', end='***')
print('Привет', end='***')
print(123, end='***')
print(1, 2, 3)
print(1, 2, 3, sep='#')

# Input

line = input()
print(line)

line = input('Введите строку: ')
print(line)

number = input('Введите число: ')
print(number + number)

number = int(input('Введите число: '))
print(number + number)

# One line input

numbers = input('введите два числа: ').split()
print(numbers)
x = int(numbers[0])
y = int(numbers[1])
print(x, y)

x, y = map(int, input('введите два числа: ').split())
print(x, y)
