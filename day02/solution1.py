with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def is_valid(level: list[int]) -> bool:
    differences = {a - b for a, b in zip(level[1:], level[:-1])}
    return differences <= {1, 2, 3} or differences <= {-1, -2, -3}


levels = [[int(i) for i in l.split()] for l in lines]
print(sum(is_valid(level) for level in levels))
