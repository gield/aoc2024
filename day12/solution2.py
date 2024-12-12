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


CORNERS = [
    ((0, -1), (-1, -1), (-1, 0)),  # top left
    ((-1, 0), (-1, 1), (0, 1)),  # top right
    ((0, 1), (1, 1), (1, 0)),  # bottom right
    ((1, 0), (1, -1), (0, -1)),  # bottom left
]
IS_CORNER = {
    (False, False, False),  # convex corner
    (True, False, True),  # concave corner
    (False, True, False),  # convex corner with same region diagonally
}


seen = set()
total = 0
for y in range(max_y):
    for x in range(max_x):
        if (y, x) in seen:
            continue
        region = floodfill(grid, y, x)
        seen |= region
        area = len(region)
        sides = sum(
            tuple((yi + dy, xi + dx) in region for dy, dx in corner) in IS_CORNER
            for corner in CORNERS
            for (yi, xi) in region
        )
        total += area * sides
print(total)
