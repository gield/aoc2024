import re

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

total = 0
for i in range(0, len(lines), 4):
    p = r"[XY].(\d+)"
    s = "".join(lines[i : i + 3])
    xa, ya, xb, yb, xp, yp = map(int, re.findall(p, s))
    xp += 10_000_000_000_000
    yp += 10_000_000_000_000

    costs = []
    b = (xp * ya - xa * yp) // (xb * ya - xa * yb)
    a = (yp - yb * b) // ya
    if xa * a + xb * b == xp and ya * a + yb * b == yp:
        costs.append(3 * a + b)
    total += min(costs) if costs else 0
print(total)

# ya * a + yb * b = yp
# a = (yp - yb * b) / ya

# xa * a + xb * b = xp
# (xa * yp - xa * yb * b) / ya + xb * b = xp
# b * (xb - xa * yb / ya) = (xp * ya) / ya - (xa * yp) / ya
# b = (xp * ya - xa * yp) / (xb * ya - xa * yb)
