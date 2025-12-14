batteries = open("input.txt").read().splitlines()

battery_sum = 0

for bat_row in batteries:
    first = (0, 0)  # (bat, pos)
    second = (0, 0)

    prev = (0, 0)
    for p, b in enumerate(bat_row[:-1]):
        b = int(b)
        p = int(p)
        if b > first[0]:
            first = (b, p)

    prev = (0, 0)
    for p, b in enumerate(bat_row[(first[1] + 1):]):
        b = int(b)
        p = int(p)
        if b > second[0]:
            second = (b, p)

    row_sum = first[0] * 10 + second[0]
    battery_sum += row_sum
    #print(row_sum, battery_sum)
        
print(battery_sum)