import operator

sum = 0
letters = {}

for line in open("input.txt").readlines():
    letters.clear()
    l_list = []

    line_data = line.strip()[:-10]
    line_sum = int(line.strip()[-10:-7])
    line_cs = line.strip()[-6:-1]
    print(line_data)
    print(line_sum)
    print(line_cs)

    for l in line.strip()[:-10]:
        if l != '-':
            try:
                letters.update({l: letters[l] + 1})
            except KeyError:
                letters.update({l : 1})

        if l.isnumeric():
            break

    for k, v in letters.items():
        l_list.append(str(v) + k)

    print(l_list)
    l_list.sort()
    print(l_list)

    i = 0
    j = 0
    s = ""
    for i in range(9, 0, -1):
        for l in l_list:
            if int(l[0]) == i:
                s = s + l[1]
                j = j + 1

                if j == 5:
                    break

            if j == 5:
                break

        if j == 5:
            break

    print(s)

    print(s == line_cs)
    if s == line_cs:
        sum = sum + line_sum

print(sum)

print("end")
