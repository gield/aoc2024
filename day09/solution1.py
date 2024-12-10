with open("input.txt", "r") as f:
    line = f.read().strip()

block_counts = list(map(int, line))
disk = []
for i, n in enumerate(block_counts):
    value = None if i % 2 else i // 2
    disk += [value] * n

for i in range(len(disk)):
    if i == len(disk) - 1:
        break
    while disk[i] is None:
        disk[i] = disk.pop()

print(sum(i * value for i, value in enumerate(disk) if value is not None))
