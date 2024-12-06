with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

ALL_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_loop(lines: list[str], start_y: int, start_x: int, obstruction_y: int, obstruction_x: int) -> bool:
    y, x, d = start_y, start_x, 0
    visited = set()
    while True:
        visited.add((y, x, d))
        dy, dx = ALL_DIRECTIONS[d]
        if (y + dy, x + dx, d) in visited:
            return True
        elif not (0 <= y + dy < max_y and 0 <= x + dx < max_x):
            break
        elif lines[y + dy][x + dx] == "#" or (y + dy == obstruction_y and x + dx == obstruction_x):
            d = (d + 1) % 4
        else:
            y, x = y + dy, x + dx
    return False


max_y, max_x = len(lines), len(lines[0])
for yi in range(max_y):
    for xi in range(max_x):
        if lines[yi][xi] == "^":
            start_y, start_x = yi, xi

y, x = start_y, start_x
d = 0
path = set()
while 0 <= y < max_y and 0 <= x < max_x:
    path.add((y, x))
    dy, dx = ALL_DIRECTIONS[d]
    if lines[y + dy][x + dx] == "#":
        d = (d + 1) % 4
    else:
        y, x = y + dy, x + dx

print(sum(is_loop(lines, start_y, start_x, yi, xi) for yi, xi in path))
