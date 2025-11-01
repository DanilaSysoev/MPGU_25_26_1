def roots_cnt(a: float, b: float, c: float) -> int:
    if a == 0:
        if b == 0 and c == 0:
            raise RuntimeError()
        elif b == 0:
            return 0
        else:
            return 1
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return 0
        elif d == 0:
            return 1
        else:
            return 2

def even_cnt(lst: list[int]) -> int:
    cnt = 0
    for item in lst:
        if item % 2 == 0:
            cnt += 1
    return cnt

def mean_points(prefix: str, points: dict[str, float]) -> float:
    summ = 0
    count = 0
    for name, point in points.items():
        if name.startswith(prefix):
            summ += point
            count += 1
    return summ / count

# a, b, c = map(float, input().split())
# print(roots_cnt(a, b, c))

data = {
    "Алексеев А.": 85,
    "Артамонов А.": 80,
    "Астафьев А.": 82,
    "Борисов Б.": 78,
    "Белкин Б.": 85,
    "Васильев В.": 92,
    "Григорьев Г.": 88,
    "Дмитриев Д.": 95,
    "Егоров Е.": 70,
    "Жуков Ж.": 88,
    "Захаров З.": 90,
    "Иванов И.": 85,
    "Кузнецов К.": 85,
    "Леонтьев Л.": 75,
}

print(mean_points("А", data))
