from collections import defaultdict


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

numbers = list(map(int, lines))
buyers: defaultdict[tuple[int, ...], int] = defaultdict(int)
for n in numbers:
    prices = [int(str(n)[-1])]
    for _ in range(2000):
        n = n ^ (n * 64) % 16777216
        n = n ^ (n // 32) % 16777216
        n = n ^ (n * 2048) % 16777216
        prices.append(int(str(n)[-1]))
    changes = [b - a for a, b in zip(prices, prices[1:])]
    pattern_to_price = {}
    for i in range(4, len(prices)):
        pattern: tuple[int, ...] = tuple(changes[i - 4 : i])
        if pattern not in pattern_to_price:
            pattern_to_price[pattern] = prices[i]
    for pattern, price in pattern_to_price.items():
        buyers[pattern] += price
print(max(buyers.values()))
