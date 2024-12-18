import math
import re
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

max_x, max_y = 101, 103
robots = [tuple(map(int, re.findall(r"[-\d]+", line))) for line in lines]

for _ in range(100):
    robots = [((x + vx) % max_x, (y + vy) % max_y, vx, vy) for x, y, vx, vy in robots]

mid_x, mid_y = max_x // 2, max_y // 2
d: defaultdict[tuple[int, int], int] = defaultdict(int)
for x, y, _, _ in robots:
    if x == mid_x or y == mid_y:
        continue
    d[(x < mid_x, y < mid_y)] += 1
print(math.prod(d.values()))
