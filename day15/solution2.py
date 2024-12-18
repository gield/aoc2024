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
        tile = lines_grid[y][x]
        grid[y, 2 * x] = {"O": "[", "#": "#", ".": ".", "@": "@"}[tile]
        grid[y, 2 * x + 1] = {"O": "]", "#": "#", ".": "..", "@": "."}[tile]
        if tile == "@":
            robot_y, robot_x = y, 2 * x
max_x *= 2

for move in moves:
    dy, dx = MOVE_DIRECTIONS[move]
    queue = [(robot_y, robot_x)]
    boxes_to_move = []
    is_wall = False
    while queue:
        y, x = queue.pop(0)
        if (y, x) in boxes_to_move:
            continue
        boxes_to_move.append((y, x))
        y_next, x_next = y + dy, x + dx
        match grid[y_next, x_next]:
            case "#":
                is_wall = True
                break
            case "[":
                queue.append((y_next, x_next))
                queue.append((y_next, x_next + 1))
            case "]":
                queue.append((y_next, x_next))
                queue.append((y_next, x_next - 1))

    if is_wall:
        continue

    while boxes_to_move:
        y, x = boxes_to_move.pop(0)
        y_next, x_next = y + dy, x + dx
        if (y_next, x_next) in boxes_to_move:
            # first need to move box ahead of this one
            boxes_to_move.append((y, x))
        else:
            grid[y_next, x_next] = grid[y, x]
            grid[y, x] = "."

    robot_y, robot_x = robot_y + dy, robot_x + dx

print(sum(100 * y + x for (y, x), tile in grid.items() if tile == "["))
