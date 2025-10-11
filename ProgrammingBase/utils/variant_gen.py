"""
Генератор вариантов заданий.
Каждый вариант содержит:
- 2 номера задач из блока A (1–4)
- 2 номера задач из блока B (5–8)
- 2 номера задач из блока C (9–12)

Пример:
    python gen_variants.py 10 output.txt --seed 42
"""

import argparse
import random

BLOCK_A = list(range(1, 5))   # 1–4
BLOCK_B = list(range(5, 9))   # 5–8
BLOCK_C = list(range(9, 13))  # 9–12
BLOCK_D = list(range(13, 17))  # 9–12

def generate_variants(n_students: int, seed: int | None = None) -> list[list[int]]:
    if seed is not None:
        random.seed(seed)

    variants = []
    for _ in range(n_students):
        a = random.sample(BLOCK_A, 1)
        b = random.sample(BLOCK_B, 1)
        c = random.sample(BLOCK_C, 1)
        d = random.sample(BLOCK_D, 1)
        variant = sorted(a + b + c + d)
        variants.append(variant)
    return variants

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="число студентов")
    parser.add_argument("output", type=str, help="имя выходного файла")
    parser.add_argument("--seed", type=int, help="фиксированный seed для воспроизводимости")
    args = parser.parse_args()

    variants = generate_variants(args.n, args.seed)

    with open(args.output, "w", encoding="utf-8") as f:
        for i, v in enumerate(variants, 1):
            f.write(f"Студент {i}: задачи {', '.join(map(str, v))}\n")

if __name__ == "__main__":
    main()
