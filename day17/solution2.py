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


def dfs(a: int, i: int) -> bool:
    # Build a, starting from the end of the program, per 3 bits
    for j in range(8):
        if run(a * 8 + j) == program[i:]:
            if i == 0:
                print(a * 8 + j)
                return True
            if n := dfs(a * 8 + j, i - 1):
                return n
    return False


dfs(0, len(program) - 1)
