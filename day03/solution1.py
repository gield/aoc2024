import re


with open("input.txt", "r") as f:
    line = f.read().strip()

multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
print(sum(int(a) * int(b) for a, b in multiplications))
