list_1 = []  # empty list, list()
print(list_1)

list_2 = [1, "one", 1.0, True]
print(list_2, id(list_2))

list_2[0] = 2
list_2[1] = "two"
list_2[2] = 2.0
print(list_2, id(list_2))

list_2.append(3)
print(list_2)

list_2.insert(2, "three")
print(list_2)

list_2.remove('two')
print(list_2)

list_2.append(3)
list_2.append(3)
list_2.remove(3)
print(list_2)

del list_2[4]
print(list_2)

print(len(list_2))

print(list_2.index('three'))
# print(list_2.index('four'))

print('three' in list_2)
print('four' in list_2)

## Slices

list_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice_1 = list_3[2:5]
print(slice_1)

slice_2 = list_3[:7]
print(slice_2)

slice_3 = list_3[3:]
print(slice_3)

slice_4 = list_3[:]
print(slice_4)

list_4 = list_3  # это не копирование

slice_5 = list_3[3:9:2]
print(slice_5)

#--------------------------------------------

list_4[3:5] = [10, 20, 30, 40]
print(list_4)

list_4[3:8:2] = [100, 200, 300]
print(list_4)

#--------------------------------------------

list_5 = [0, 1, 2, 3, 4, 5]

print(list_5[-1])
print(list_5[-len(list_5)])

#--------------------------------------------

print(list_5[-1:-3:-1])
print(list_5[-1:-300:-1])

#--------------------------------------------
