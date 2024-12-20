import heapq

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
max_y, max_x = len(lines), len(lines[0])
grid = {}
for y in range(max_y):
    for x in range(max_x):
        grid[y, x] = lines[y][x]
        if grid[y, x] == "S":
            start_y, start_x = y, x
        if grid[y, x] == "E":
            end_y, end_x = y, x

queue = [(0, start_y, start_x, [(start_y, start_x)])]
seen = {(start_y, start_x)}
while queue:
    score, y, x, path = heapq.heappop(queue)
    if y == end_y and x == end_x:
        break
    for dy, dx in DIRECTIONS:
        if (y + dy, x + dx) in seen or grid[y + dy, x + dx] in {"", "#"}:
            continue
        seen.add((y + dy, x + dx))
        heapq.heappush(queue, (score + 1, y + dy, x + dx, path + [(y + dy, x + dx)]))

num_shortcuts = 0
for i in range(len(path)):
    yi, xi = path[i]
    for j in range(i + 2, len(path)):
        yj, xj = path[j]
        cheat = abs(yi - yj) + abs(xi - xj)
        if cheat <= 20 and j - i - cheat >= 100:
            num_shortcuts += 1
print(num_shortcuts)
