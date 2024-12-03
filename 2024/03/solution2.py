import re

muls = open("input.txt").read()

total_sum = 0
multiply = True
muls = re.findall(r'(do)\(\)|(don)\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', muls)
#print(muls)

for mul in muls:
    #print(mul)
    do, don, p1, p2 = mul

    if do == "do":
        multiply = True
        continue

    if don == "don":
        multiply = False
        continue

    if multiply:
        #print(p1, p2)
        total_sum = total_sum + (int(p1) * int(p2))

print(total_sum)