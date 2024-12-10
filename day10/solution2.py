from collections import defaultdict


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

max_y, max_x = len(lines), len(lines[0])
d = {(y, x): int(lines[y][x]) for y in range(max_y) for x in range(max_x)}
zeros = [coord for coord, n in d.items() if n == 0]
grid = defaultdict(int, d)

num_routes = 0
for zy, zx in zeros:
    queue = [(zy, zx, 0)]
    while len(queue):
        y, x, n = queue.pop(0)
        if n == 9:
            num_routes += 1
            continue
        for dy, dx in DIRECTIONS:
            if grid[y + dy, x + dx] == n + 1:
                queue.append((y + dy, x + dx, n + 1))
print(num_routes)
