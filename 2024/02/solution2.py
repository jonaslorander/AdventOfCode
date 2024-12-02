rows = open("input.txt").read().splitlines()

total_safe = 0

def recheck_safety(reports):
    last_increasing = None
    this_increasing = None
    print("B", reports)
    for i in range(len(reports) - 1):
        diff = int(reports[i]) - int(reports[i + 1])

        if diff > 0:
            this_increasing = False
        elif diff < 0:
            this_increasing = True

        if abs(diff) not in range(1, 4):
            return False

        if (this_increasing != last_increasing) and last_increasing != None:
            return False
        
        last_increasing = this_increasing
    
    return True

def check_safety(row):
    last_increasing = None
    this_increasing = None
    reports0 = row.split(" ")
    print("A", reports0)
    for i in range(len(reports0) - 1):
        diff = int(reports0[i]) - int(reports0[i + 1])

        #print(diff)
        if diff > 0:
            this_increasing = False
        elif diff < 0:
            this_increasing = True

        if diff == 0:
            reports1 = list(reports0)
            reports2 = list(reports0)
            reports0.pop(i)
            reports1.pop(i + 1)
            reports2.pop(i - 1)
            return recheck_safety(reports0) or recheck_safety(reports1) or recheck_safety(reports2)

        if abs(diff) not in range(1, 4):
            reports1 = list(reports0)
            reports2 = list(reports0)
            reports0.pop(i)
            reports1.pop(i + 1)
            reports2.pop(i - 1)
            return recheck_safety(reports0) or recheck_safety(reports1) or recheck_safety(reports2)

        #print(this_increasing)
        if (this_increasing != last_increasing) and last_increasing != None:
            reports1 = list(reports0)
            reports2 = list(reports0)
            reports0.pop(i)
            reports1.pop(i + 1)
            reports2.pop(i - 1)
            return recheck_safety(reports0) or recheck_safety(reports1) or recheck_safety(reports2)
        
        last_increasing = this_increasing
    
    return True

for row in rows:
    is_safe = check_safety(row)
    if is_safe:
        total_safe = total_safe + 1
    else:
        print(False)
        pass

print(total_safe)
