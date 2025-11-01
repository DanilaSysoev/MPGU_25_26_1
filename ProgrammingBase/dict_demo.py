data = {
    "one": 1,
    "two": 2,
    "three": 3,
}

print(data["one"])
print(data["two"])

# print(data["four"])

data["one"] = 100
data["four"] = 400

print(data)

data.update({"five": 500, "six": 600, "three": 300})
print(data)

for key in data.keys():
    print(key, end=' ')
print()

for value in data.values():
    print(value, end=' ')
print()

for key, value in data.items():
    print(f"{key}: {value}")
print()

for key in data:
    print(key, end=' ')
print()

print("one" in data)
