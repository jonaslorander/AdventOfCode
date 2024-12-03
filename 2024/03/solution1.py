import re

muls = open("input.txt").read()

total_sum = 0
muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', muls)

for mul in muls:
    p1, p2 = mul
    total_sum = total_sum + (int(p1) * int(p2))

print(total_sum)
