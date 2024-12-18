import itertools
import re


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

max_x, max_y = 101, 103
robots = [tuple(map(int, re.findall(r"[-\d]+", line))) for line in lines]

for i in itertools.count():
    robots = [((px + vx) % max_x, (py + vy) % max_y, vx, vy) for px, py, vx, vy in robots]

    print(i + 1)
    coords = {(x, y) for x, y, _, _ in robots}
    for x in range(max_x):
        for y in range(max_y):
            if (y, x) in coords:
                print("█", end="")
            else:
                print(" ", end="")
        print()
    input()
