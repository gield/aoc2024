import itertools

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
raw_registers = lines[:empty_line_i]
raw_program = lines[empty_line_i + 1]

original_registers = [int(register.split(" ")[-1]) for register in raw_registers]
program = list(map(int, raw_program.split(" ")[1].split(",")))


def run(a: int) -> list[int]:
    # Manual conversion of the program into python
    output = []
    while a:
        b = (a % 8) ^ 3
        c = a >> b
        a = a >> 3
        b = (b ^ 5) ^ c
        output.append(b % 8)
    return output


for a in itertools.count(78_732_909, 2_097_152):
    if a & 2**47 != 2**47:  # 100000000000000000000000000000000000000000000000
        continue
    if a & 2**40 != 2**40:  # 10000000000000000000000000000000000000000
        continue
    if a & 2**37 != 2**37:  # 10000000000000000000000000000000000000
        continue
    if a & 2**32 != 2**32:  # 100000000000000000000000000000000
        continue
    if a & 2**26 != 2**26:  # 100000000000000000000000000
        continue
    if a & 2**20 != 2**20:  # 100000000000000000000
        continue
    if a & 24173 != 24173:  # 101111001101101
        continue
    if a & 2**15 != 0:  # 1000000000000000
        continue
    if a & 2**8 != 0:  # 100000000
        continue

    if run(a) == program:
        print(a)
        break
