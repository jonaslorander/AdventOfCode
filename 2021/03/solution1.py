reports = open("input.txt").read().splitlines()

epsilon = ""
gamma = ""

for i in range(len(reports[0])):
    H = 0
    L = 0
    for report in reports:
        if report[i] == '1':
            H = H + 1
        else:
            L = L + 1

    if H > L:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"{gamma * epsilon}")