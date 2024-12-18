with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

empty_line_i = lines.index("")
raw_registers = lines[:empty_line_i]
raw_program = lines[empty_line_i + 1]

registers = [int(register.split(" ")[-1]) for register in raw_registers]
program = list(map(int, raw_program.split(" ")[1].split(",")))

pointer = 0
output = []
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer + 1]
    combo_operand = operand if operand <= 3 else registers[operand - 4]

    match opcode:
        case 0:  # adv
            registers[0] = registers[0] // 2**combo_operand
        case 1:  # bxl
            registers[1] = registers[1] ^ operand
        case 2:  # bst
            registers[1] = combo_operand % 8
        case 3:  # jnz
            if registers[0] != 0:
                pointer = operand
                continue
        case 4:  # bxc
            registers[1] = registers[1] ^ registers[2]
        case 5:  # out
            output.append(combo_operand % 8)
        case 6:  # bdv
            registers[1] = registers[0] // 2**combo_operand
        case 7:  # cdv
            registers[2] = registers[0] // 2**combo_operand

    pointer += 2

print(",".join(map(str, output)))
