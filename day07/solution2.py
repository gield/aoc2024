from functools import reduce
from itertools import product
from operator import add, mul
from typing import Callable


with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")


def execute_operator(s: int, t: tuple[Callable[[int, int], int], int]) -> int:
    op, n = t
    return op(s, n)


total = 0
operations = [add, mul, lambda a, b: int(f"{a}{b}")]
for l in lines:
    test_value, *numbers = map(int, l.replace(":", "").split(" "))
    for operators in product(operations, repeat=len(numbers) - 1):
        solution = reduce(execute_operator, zip(operators, numbers[1:]), numbers[0])
        if solution == test_value:
            total += test_value
            break
print(total)
