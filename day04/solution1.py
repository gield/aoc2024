from collections import defaultdict
from typing import Callable


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def groups(matrix: list[str], func: Callable[[int, int], int]) -> list[str]:
    # https://stackoverflow.com/a/43311126/940918
    grouping = defaultdict(list)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            grouping[func(x, y)].append(matrix[y][x])
    return ["".join(grouping[g]) for g in sorted(grouping)]


horizontal = lines
vertical = groups(lines, lambda x, _: x)
diagonal_f = groups(lines, lambda x, y: x + y)
diagonal_b = groups(lines, lambda x, y: x - y)
print(sum(l.count("XMAS") + l.count("SAMX") for l in vertical + horizontal + diagonal_f + diagonal_b))
