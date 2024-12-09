disk = open("input.txt").read().strip()
frag = []

class Block():
    def __init__(self, value, size):
        self.size = size
        self.value = value
        self.empty = True if value == '.' else False

    def __repr__(self):
        return f"|{self.value if not self.empty else 'E'}*{self.size}|"
    
    def flatten(self):
        if self.empty:
            return ['.'] * int(self.size)
        else:
            return [self.value] * int(self.size)

id = 0
for i, v in enumerate(disk):
    if not i % 2:
        frag.append(Block(str(id), int(v))) 
        id += 1
    else:
        if int(v) > 0:
            frag.append(Block('.', int(v)))

fragcopy = list(frag)

i = len(frag) - 1
while i > 0:
    if not frag[i].empty:
        for j, v in enumerate(frag[:i]):
            if v.empty:
                # Can the data fit in the empty range?
                if frag[i].size <= v.size:
                    # If so remove it from the list and put it in the empty space replacing the data with empty space
                    frag[j] = frag[i]
                    frag[i] = Block('.', frag[i].size)
                    if frag[i].size < v.size:
                        frag.insert(j + 1, Block('.', (v.size - frag[i].size)))
                        # Increase array pointer since we are adding an extra item before it
                        i += 1
                    
                    # Concatenate empty blocks
                    for k, b in enumerate(frag):
                        if b.empty and k < len(frag) - 1:
                            if frag[k + 1].empty:
                                frag[k] = Block('.', (b.size + frag[k + 1].size))
                                frag.pop(k + 1)

                    # If data moved, check next block of data to move
                    break
    i -= 1

# Flatten blocks and add them
defrag = []
for b in frag:
    defrag.append(b.flatten())

defrag = [block for blocks in defrag for block in blocks]

# Calculate checksum
checksum = 0
for id, block in enumerate(defrag):
    if not '.' in block:
        checksum += id * int(block)

print(f"Checksum is {checksum}")
