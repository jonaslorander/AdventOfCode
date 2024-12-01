import re

rows = open("input.txt").read().splitlines()

def replace_number(s):
    return s.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e") \
        .replace("four", "f4r").replace("five", "f5e").replace("six", "s6x") \
        .replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")

total = 0
for row in rows:
    r = replace_number(row)
    numbers = re.findall(r'\d', r)
    number = int(f"{numbers[0]}{numbers[-1]}")
    total = total + number

print(total)