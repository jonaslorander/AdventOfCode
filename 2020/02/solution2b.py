lines = open("input.txt").read().splitlines()

passwords = []
for line in lines:
    passwords.append(line.strip(":").split())

cp = 0 # Correct passwords counter

for pw in passwords:
    positions = pw[0].split("-")
    p1 = int(positions[0]) - 1
    p2 = int(positions[1]) - 1
    char = pw[1].strip(":")
    password = pw[2]

    if (password[p1] == char and password[p2] != char) or (password[p1] != char and password[p2] == char):
        cp = cp + 1

print(f"Valid passwords: {cp}.")
