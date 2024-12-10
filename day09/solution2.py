with open("input.txt", "r") as f:
    line = f.read().strip()

block_counts = list(map(int, line))
disk = []
for i, blocks_needed in enumerate(block_counts):
    if i % 2:
        for j in range(len(block_counts) - 1, i, -2):
            if block_counts[j] == 0:
                continue
            if block_counts[j] <= blocks_needed:
                disk += [j // 2] * block_counts[j]
                blocks_needed -= block_counts[j]
                block_counts[j] = 0
            if blocks_needed == 0:
                break
        disk += [0] * blocks_needed
    elif blocks_needed > 0:
        disk += [i // 2] * blocks_needed
    else:
        disk += [0] * int(line[i])

print(sum(i * value for i, value in enumerate(disk)))
