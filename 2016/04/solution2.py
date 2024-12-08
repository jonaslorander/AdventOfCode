a = "abcdefghijklmnopqrstuvwxyz"

def chipher(n, id):
    d = ""
    for l in n:
        if l == '-':
            d = d + ' '
        else:
            r = id % 26 # 26 letters in alphabet
            c = ord(l)

            if r + c <= ord('z'):
                d = d + chr(c + r)
            else:
                d = d + chr(c + r - 26)

    return d


for line in open("input.txt").readlines():
    room_name = line.strip()[:-11]
    room_id = int(line.strip()[-10:-7])

#    print(room_name)
#    print(room_id)

    c = chipher(room_name, room_id)
#    print(c)
    
    if c[:5] == "north":# pole objects":
        print("North pole objects are in room " + str(room_id))
        break

print("end")
