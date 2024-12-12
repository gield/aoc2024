from collections import defaultdict


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_y, max_x = len(lines), len(lines[0])
d = {(y, x): lines[y][x] for y in range(max_y) for x in range(max_x)}
grid = defaultdict(str, d)


def floodfill(grid: defaultdict[tuple[int, int], str], y: int, x: int) -> set[tuple[int, int]]:
    region = {(y, x)}
    queue = [(y, x)]
    while len(queue):
        y, x = queue.pop(0)
        region.add((y, x))
        for dy, dx in DIRECTIONS:
            if (y + dy, x + dx) in region or (y + dy, x + dx) in queue:
                continue
            if grid[y + dy, x + dx] == grid[y, x]:
                queue.append((y + dy, x + dx))
    return region


seen = set()
total = 0
for y in range(max_y):
    for x in range(max_x):
        if (y, x) in seen:
            continue
        region = floodfill(grid, y, x)
        seen |= region
        area = len(region)
        perimeter = 4 * area
        for yi, xi in region:
            for dy, dx in DIRECTIONS:
                if grid[yi + dy, xi + dx] == grid[y, x]:
                    perimeter -= 1
        total += area * perimeter
print(total)
