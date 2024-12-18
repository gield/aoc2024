import heapq
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start_y, start_x = 0, 0
max_y, max_x = 70, 70
grid = defaultdict(str, {(y, x): "." for y in range(max_y + 1) for x in range(max_x + 1)})
coords = [tuple(map(int, l.split(","))) for l in lines]


def find_path(grid: defaultdict[tuple[int, int], str]) -> bool:
    found = False
    queue = [(0, start_y, start_x)]
    seen = {(start_y, start_x)}
    while queue:
        score, y, x = heapq.heappop(queue)
        if y == max_y and x == max_x:
            found = True
            break
        for dy, dx in DIRECTIONS:
            if (y + dy, x + dx) in seen or grid[y + dy, x + dx] in {"", "#"}:
                continue
            seen.add((y + dy, x + dx))
            heapq.heappush(queue, (score + 1, y + dy, x + dx))
    return found


for i in range(1024, len(coords)):
    grid_new = grid.copy()
    for x, y in coords[:i]:
        grid_new[y, x] = "#"
    if not find_path(grid_new):
        print(coords[i - 1])
        break
