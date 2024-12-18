with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


MOVE_DIRECTIONS = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
}

empty_line_i = lines.index("")
lines_grid = lines[:empty_line_i]
moves = "".join(lines[empty_line_i:])

max_y, max_x = len(lines_grid), len(lines_grid[0])
grid = {}
for y in range(max_y):
    for x in range(max_x):
        grid[y, x] = lines_grid[y][x]
        if grid[y, x] == "@":
            robot_y, robot_x = y, x

for move in moves:
    dy, dx = MOVE_DIRECTIONS[move]
    for d in range(1, max(max_y, max_x)):
        y, x = robot_y + d * dy, robot_x + d * dx
        if grid[y, x] in "#.":
            is_wall = grid[y, x] == "#"
            max_d = d
            break

    if is_wall:
        continue

    for d in range(max_d, 0, -1):
        y, x = robot_y + d * dy, robot_x + d * dx
        grid[y, x] = grid[y - dy, x - dx]

    grid[robot_y, robot_x] = "."
    robot_y, robot_x = robot_y + dy, robot_x + dx

print(sum(100 * y + x for (y, x), tile in grid.items() if tile == "O"))
