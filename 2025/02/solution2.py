ids = open("input.txt").read().replace('\r', '').replace('\n', '').split(',')

def get_chunks(lst, n):
    ret_list = []
    for i in range(0, len(lst), n):
        ret_list.append(lst[i:i + n])

    return ret_list

def find_invalid_ids(start, stop):
    id_list = list(range(int(start), int(stop) + 1))
    id_list = [str(id) for id in id_list]
    sum = 0

    for id in id_list:
        i = 1
        while i <= len(id) / 2:
            chunks = get_chunks(id, i)
            equal = all(c == chunks[0] for c in chunks)
            i += 1

            if equal:
                sum += int(id)
                break

    return sum

invalid_sum = 0
for id_range in ids:
    id_range = id_range.split('-')
    invalid_sum = invalid_sum + find_invalid_ids(id_range[0], id_range[1])

print(invalid_sum)
