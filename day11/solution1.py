with open("input.txt", "r") as f:
    line = f.read().strip()

stones = list(map(int, line.split()))
for _ in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            new_stones.append(int(str(stone)[:mid]))
            new_stones.append(int(str(stone)[mid:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
print(len(stones))
