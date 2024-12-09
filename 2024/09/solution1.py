disk = open("input.txt").read().strip()
frag = []

id = 0
for i, v in enumerate(disk):
    if not i % 2:
        for _ in range(int(v)):
            frag.append(str(id)) 
        id += 1
    else:
        for _ in range(int(v)):
            frag.append('.') 

defrag = []
fragcopy = list(frag)
for i, v in enumerate(frag):
    if v == '.':
        last_block = fragcopy.pop(-1)
        while last_block == '.':
            last_block = fragcopy.pop(-1)
        defrag.append(last_block)
    else:
        defrag.append(v)

    if len(defrag) >= len(fragcopy):
        break

# Calculate checksum
checksum = 0
for id, data in enumerate(defrag):
    checksum += id * int(data)

print(f"Checksum is {checksum}")

