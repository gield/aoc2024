with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

patterns = lines[0].split(", ")


def dfs(design: str, memo: dict[str, int]) -> int:
    if design == "":
        return 1
    if design in memo:
        return memo[design]

    num_possible = 0
    for p in patterns:
        if design.startswith(p):
            num_possible += dfs(design[len(p) :], memo)

    memo[design] = num_possible
    return num_possible


print(sum(dfs(design, {}) for design in lines[2:]))
