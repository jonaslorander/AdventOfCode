import re

rows = open("input.txt").read().splitlines()

sum = 0
for row in rows:
    numbers = re.findall(r'\d', row)
    number = int("".join([numbers[0], numbers[-1]]))
    sum = sum + number

print(sum)