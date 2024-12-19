with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

patterns = lines[0].split(", ")


def dfs(design: str) -> bool:
    if design == "":
        return True

    for p in patterns:
        if design.startswith(p):
            if dfs(design[len(p) :]):
                return True

    return False


print(sum(dfs(design) for design in lines[2:]))
