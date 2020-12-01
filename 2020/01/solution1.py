reports = open("input.txt").read().split('\n')[:-1]

fact1 = fact2 = 0

for r in reports:
    ri = int(r)

    for n in reports:
        ni = int(n)
        if ri + ni == 2020:
            fact1 = ri
            fact2 = ni

            break

    if fact1 + fact2 != 0:
        break

print(f'{fact1} * {fact2} = {fact1 * fact2}')

fact1 = fact2 = fact3 = 0

for r in reports:
    ri = int(r)

    for n in reports:
        ni = int(n)

        for m in reports:
            mi = int(m)
            if ri + ni + mi == 2020:
                fact1 = ri
                fact2 = ni
                fact3 = mi

                break
            
        if fact1 + fact2 + fact3 != 0:
            break

    if fact1 + fact2 + fact3 != 0:
        break

print(f'{fact1} * {fact2} * {fact3} = {fact1 * fact2 * fact3}')