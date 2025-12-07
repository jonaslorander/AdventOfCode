ids = open("input.txt").read().replace('\r', '').replace('\n', '').split(',')

def find_invalid_ids(start, stop):
    id_list = list(range(int(start), int(stop) + 1))
    id_list = [str(id) for id in id_list]

    sum = 0
    for id in id_list:
        if id[0:int(len(id)/2)] == id[int(len(id)/2):len(id)]:
            sum = sum + int(id)

    return sum

invalid_sum = 0
for id_range in ids:
    id_range = id_range.split('-')
    invalid_sum = invalid_sum + find_invalid_ids(id_range[0], id_range[1])

print(invalid_sum)