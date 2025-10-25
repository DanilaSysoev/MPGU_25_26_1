data = [6, 1, 2, 9, 4, 2]

for item in data:
    print(item)    
    
for index, item in enumerate(data):
    print(f'{index}: {item}')

for i in range(10):
    print(i)
print('-' * 30)

for i in range(10, 20):
    print(i)
print('-' * 30)
    
for i in range(10, 30, 2):
    print(i)
print('-' * 30)

for index in range(len(data)):
    print(data[index])
print('-' * 30)
    
for i in range(10, 0, -1):
    print(i)

range_data = list(range(20))

print(range_data[5])
print(range_data[-5])
