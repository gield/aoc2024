with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

ALL_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

max_y, max_x = len(lines), len(lines[0])
for yi in range(max_y):
    for xi in range(max_x):
        if lines[yi][xi] == "^":
            start_y, start_x = yi, xi

y, x, d = start_y, start_x, 0
visited = set()
while y in range(max_y) and x in range(max_x):
    visited.add((y, x))
    dy, dx = ALL_DIRECTIONS[d]
    if lines[y + dy][x + dx] == "#":
        d = (d + 1) % 4
    else:
        y, x = y + dy, x + dx
print(len(visited))
