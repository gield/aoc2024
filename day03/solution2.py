import re


with open("input.txt", "r") as f:
    line = f.read().strip()

operations = re.findall(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)", line)
total = 0
enabled = True
for do, dont, a, b in operations:
    if do or dont:
        enabled = bool(do)
        continue
    if enabled:
        total += int(a) * int(b)
print(total)
