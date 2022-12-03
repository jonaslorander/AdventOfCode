bags = open("input.txt").read().split("\n")

single_carachters = []
sum = 0
for things in bags:
    compartments = []
    compartments.append(things[:len(things)//2])
    compartments.append(things[len(things)//2:])

    single_char = ""
    for char in compartments[0]:
        if char in compartments[1]:
            single_char = char
            break
        else:
            continue

    char_value = (ord(char) - ord('a') + 1) if ord(char) >= ord('a') else (ord(char) - ord('A') + 27)
    sum = sum + char_value

    single_carachters.append(single_char)

print(single_carachters)
print(sum)