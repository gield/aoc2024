import functools


with open("input.txt", "r") as f:
    line = f.read().strip()


@functools.cache
def blink(stone: int, b: int) -> int:
    if b == 0:
        return 1
    if stone == 0:
        return blink(1, b - 1)
    if len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        stone_left = int(str(stone)[:mid])
        stone_right = int(str(stone)[mid:])
        return blink(stone_left, b - 1) + blink(stone_right, b - 1)
    return blink(stone * 2024, b - 1)


stones = list(map(int, line.split()))
print(sum(blink(stone, 75) for stone in stones))
