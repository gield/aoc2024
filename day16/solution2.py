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

queue = [(0, start_y, start_x, 0, [(start_y, start_x)])]
best_score = float("inf")
seen = set()
seats = set()
while queue:
    score, y, x, dir, prev = heapq.heappop(queue)
    if score > best_score:
        continue
    if y == end_y and x == end_x:
        best_score = score
        seats |= set(prev)
    seen.add((y, x, dir))
    dy, dx = DIRECTIONS[dir]
    if grid[y + dy, x + dx] != "#" and (y + dy, x + dx, dir) not in seen:
        heapq.heappush(queue, (score + 1, y + dy, x + dx, dir, prev + [(y + dy, x + dx)]))
    if (y, x, (dir + 1) % 4) not in seen:
        heapq.heappush(queue, (score + 1000, y, x, (dir + 1) % 4, prev))
    if (y, x, (dir - 1) % 4) not in seen:
        heapq.heappush(queue, (score + 1000, y, x, (dir - 1) % 4, prev))
print(len(seats))
