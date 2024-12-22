with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

numbers = list(map(int, lines))
total = 0
for n in numbers:
    for _ in range(2000):
        n = n ^ (n * 64) % 16777216
        n = n ^ (n // 32) % 16777216
        n = n ^ (n * 2048) % 16777216
    total += n
print(total)
