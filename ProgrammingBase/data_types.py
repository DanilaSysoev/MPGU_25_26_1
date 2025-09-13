'''
bool  - булевый тип (True/False)
int   - целочисленный тип (123, -12)
float - число с плавающей точкой (12.3, -1.3e5)
str   - строковый тип ("hello", 'world')
'''

# bool
b1 = True
print(id(b1))

b2 = False
print(b1, b2)

b1 = False
print(id(b1))

# int
i0 = 1000**1000
print(i0)
i1 = 123
i2 = -234
i3 = 0b1001
i4 = 0o1234
i5 = 0x123ab
i6 = 123_456_78_9
print(bool(1000))

# float
f1 = 0.1
f2 = f1 + f1 + f1
print(f2)
print(3 * f1)
f3 = 1.23
f4 = -12.5
f5 = 1.6e3  # 1.6 * 10**3
f6 = -1.6e-3

hello = 0
hello_world = 1
hello_my_world = 2

# types annotations
my_int: int = 123
