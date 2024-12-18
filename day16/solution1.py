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

queue = [(0, start_y, start_x, 0)]
seen = {(start_y, start_x, 0)}
while queue:
    score, y, x, dir = heapq.heappop(queue)
    if y == end_y and x == end_x:
        print(score)
        break
    dy, dx = DIRECTIONS[dir]
    if grid[y + dy, x + dx] != "#" and (y + dy, x + dx, dir) not in seen:
        heapq.heappush(queue, (score + 1, y + dy, x + dx, dir))
        seen.add((y + dy, x + dx, dir))
    if (y, x, (dir + 1) % 4) not in seen:
        heapq.heappush(queue, (score + 1000, y, x, (dir + 1) % 4))
        seen.add((y, x, (dir + 1) % 4))
    if (y, x, (dir - 1) % 4) not in seen:
        heapq.heappush(queue, (score + 1000, y, x, (dir - 1) % 4))
        seen.add((y, x, (dir - 1) % 4))
