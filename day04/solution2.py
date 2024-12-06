from collections import defaultdict


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

num_rows, num_cols = len(lines), len(lines[0])
d = {(r, c): lines[r][c] for r in range(num_rows) for c in range(num_rows)}
matrix = defaultdict(str, d)

print(
    sum(
        matrix[r, c] == "A"
        and matrix[r - 1, c - 1] + matrix[r + 1, c + 1] in {"MS", "SM"}
        and matrix[r - 1, c + 1] + matrix[r + 1, c - 1] in {"MS", "SM"}
        for r in range(num_rows)
        for c in range(num_cols)
    )
)
