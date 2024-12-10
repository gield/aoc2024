from collections import defaultdict


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

max_y, max_x = len(lines), len(lines[0])
frequencies = defaultdict(set)
for y in range(max_y):
    for x in range(max_x):
        if lines[y][x] != ".":
            frequencies[lines[y][x]].add((y, x))

antinodes = set()
for antennas in frequencies.values():
    pairs = [(a, b) for a in antennas for b in antennas if a != b]
    for (ya, xa), (yb, xb) in pairs:
        antinodes.add((ya, xa))
        dy, dx = ya - yb, xa - xb
        while (ya := ya + dy) in range(max_y) and (xa := xa + dx) in range(max_x):
            antinodes.add((ya, xa))
print(len(antinodes))
