# +, -, *, /
# // - целочисленное деление,
# % - остаток от деления
# ** - возведение в степень

# +=, -=, *=, /=, //=, %=, **=
# x <operator>= y    <->    x = x <operator> y


first, second = map(int, input().split())

print(f"{first} + {second} = {first + second}")
print(f"'{str(first)}' + '{str(second)}' = {str(first) + str(second)}")
print(f"{first} - {second} = {first - second}")
print(f"'{str(first)}' * {second} = {str(first) * second}")
print(f"{first} / {second} = {first / second}")
print(f"{first} // {second} = {first // second}")
print(f"{first} % {second} = {first % second}")
print(f"{first} ** {second} = {first ** second}")

# ==, !=, >, <, >=, <=

num = int(input())

print(10 < num < 20) #  (10 < num) and (num < 20)

# not, and, or
# &, |, ^, ~, <<, >>

# x      |  not x
# False  |  True
# True   |  False

# x      | y      |  x and y
# False  | False  |  False
# False  | True   |  False
# True   | False  |  False
# True   | True   |  True

# x      | y      |  x or y
# False  | False  |  False
# False  | True   |  True
# True   | False  |  True
# True   | True   |  True

# x = 131: 10000011
# y = 79:  01001111

# x & y = 00000011 -> 3
# x | y = 11001111 -> 207
# x ^ y = 11001100 -> 204
# ~x = ..101111100 -> -132
# x << 2 = 1000001100 -> 524
# y >> 2 = 00010011 -> 19 (старший бит всегда остается)
