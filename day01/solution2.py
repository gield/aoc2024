with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

left = [int(l.split()[0]) for l in lines]
right = [int(l.split()[1]) for l in lines]
print(sum(l * right.count(l) for l in left))
