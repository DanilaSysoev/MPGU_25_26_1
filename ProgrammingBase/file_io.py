with open('in.txt', 'r') as f:
    data = f.read()    
print(data)


print('-'*50)
with open('in.txt', 'r') as f:
    data = f.readlines()
print(data)


print('-'*50)
with open('in.txt', 'r') as f:
    data = f.readline()
print(data)


print('-'*50)
data = []
with open('in.txt', 'r') as f:
    for line in f:
        data.append(line)
print(data)


print('-'*50)
with open('in.txt', 'r') as f:
    data = f.read(5)
print(data)

# --------------------------------------

with open('out1.txt', 'w') as f:
    f.write('Hello')


with open('out2.txt', 'w') as f:
    f.writelines(['Hello\n', 'World\n'])


with open('out3.txt', 'a') as f:
    f.write('*')
    