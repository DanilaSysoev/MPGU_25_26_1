from datetime import datetime, timedelta

print(datetime.now())
print(datetime(2023, 1, 1))

str_d = str(datetime.now())
str_d2 = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

print(str_d, str_d2)

dt = datetime.strptime(str_d2, "%Y-%m-%d, %H:%M:%S")
print(dt)

dt_before = datetime.now() - timedelta(hours=10)
print(dt_before)

try:
    print(datetime(1990, 20, 12))
except ValueError:
    print("Invalid datetime")

data = [4, 1, 2, 6, 4, 8, 8, 1, 0]
# data.sort()

print(data)
srt = sorted(data, key=lambda v: v % 5)
print(srt)
