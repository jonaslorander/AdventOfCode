boarding_passes = open("input.txt").read().splitlines()

# F = 0
# B = 1
# L = 0
# R = 1

def get_seat_id(bp):
    bp = bp.replace("F", "0")
    bp = bp.replace("B", "1")
    bp = bp.replace("L", "0")
    bp = bp.replace("R", "1")

    row = int(bp[0:7], 2)
    col = int(bp[7:10], 2)

    sid = row * 8 + col

    return sid

seat_ids = []
for boarding_pass in boarding_passes:
    seat_ids.append(get_seat_id(boarding_pass))

# Sort seat ids
seat_ids.sort()

print(f"Highest seat id: {seat_ids[-1]}")
for i in range(len(seat_ids)):
    if seat_ids[i] + 1 != seat_ids[i + 1]:
        print(f"Your seat is {seat_ids[i] + 1}")
        break