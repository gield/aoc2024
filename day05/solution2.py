def order_correctly(rules: set[tuple[str, ...]], update: list[str]) -> list[str]:
    update = update.copy()
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                update[i], update[j] = update[j], update[i]
                return order_correctly(rules, update)
    return update


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
rules = {tuple(l.split("|")) for l in lines[:empty_line_i]}
updates = [l.split(",") for l in lines[empty_line_i + 1 :]]

total = 0
for update in updates:
    corrected_update = order_correctly(rules, update)
    if update != corrected_update:
        mid = len(corrected_update) // 2
        total += int(corrected_update[mid])
print(total)
