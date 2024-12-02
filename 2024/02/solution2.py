rows = open("input.txt").read().splitlines()

total_safe = 0

def check_safety(row):
    last_increasing = None
    this_increasing = None
    reports = row.split(" ")
    #print(reports)
    for i in range(len(reports) - 1):
        diff = int(reports[i]) - int(reports[i + 1])

        #print(diff)
        if diff > 0:
            this_increasing = False
        elif diff < 0:
            this_increasing = True

        if abs(diff) not in range(1, 4):
            return False

        #print(this_increasing)
        if (this_increasing != last_increasing) and last_increasing != None:
            return False
        
        last_increasing = this_increasing
    
    return True

for row in rows:
    is_safe = check_safety(row)
    #print(is_safe)
    if is_safe:
        total_safe = total_safe + 1

print(total_safe)
