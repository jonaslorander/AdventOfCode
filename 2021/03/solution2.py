reports = open("input.txt").read().splitlines()

def find_report(reports, HL):
    i = 0
    while(len(reports) > 1):
        H = 0
        L = 0
        for report in reports:
            if report[i] == "1":
                H = H + 1
            else:
                L = L + 1

        keep = " "
        if HL:
            if H >= L:
                keep = "1"
            else:
                keep = "0"
        else:
            if H >= L:
                keep = "0"
            else:
                keep = "1"

        reports = [r for r in reports if r[i] == keep]

        i = i + 1

    return reports[0]


o2 = int(find_report(reports, True), 2)
co2 = int(find_report(reports, False), 2)

print(f"{o2} * {co2} = {o2 * co2}")