import re

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total = 0
for i in range(0, len(lines), 4):
    p = r"[XY].(\d+)"
    s = "".join(lines[i : i + 3])
    xa, ya, xb, yb, xp, yp = map(int, re.findall(p, s))

    costs = []
    for a in range(100):
        for b in range(100):
            if xa * a + xb * b == xp and ya * a + yb * b == yp:
                costs.append(3 * a + b)
    total += min(costs) if costs else 0
print(total)
