lines = open("input.txt").read().splitlines()[:-1]

passwords = []
for line in lines:
    passwords.append(line.strip(":").split())

cp = 0 # Correct passwords counter
for pw in passwords:
    minmax = pw[0].split("-")
    min = int(minmax[0])
    max = int(minmax[1])
    char = pw[1].strip(":")
    password = pw[2]

    if min <= password.count(char) <= max:
        cp = cp + 1

print(f"Valid passwords: {cp}.")
