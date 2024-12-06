with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
rules = {tuple(l.split("|")) for l in lines[:empty_line_i]}
updates = [l.split(",") for l in lines[empty_line_i + 1 :]]
print(
    sum(
        int(update[len(update) // 2])
        for update in updates
        if all((b, a) not in rules for a, b in zip(update, update[1:]))
    )
)
