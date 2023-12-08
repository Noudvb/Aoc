with open("input.txt") as f:
    info = f.read().splitlines()

seeds = info[0].split(": ")[1].split()
seeds = [int(seed) for seed in seeds]


def trans(info, seeds):
    temp = seeds.copy()
    for index, transfer in enumerate(info):
        if transfer and transfer[0].isnumeric():
            destination, source, length = [int(num) for num in transfer.split()]
            for i, seed in enumerate(seeds):
                if source <= seed < source + length:
                    temp[i] = destination + seed - source
        else:
            seeds = temp.copy()
    return min(temp)

print('answer part 1: ', trans(info, seeds))


seeds = info[0].split(": ")[1].split()
seeds = [int(seed) for seed in seeds]

megaseeds = []
for i in range(0, len(seeds), 2):
    megaseeds.append([seeds[i], seeds[i] + seeds[i+1] - 1])

temp = []
for index, transfer in enumerate(info[3:]):
    if transfer and transfer[0].isnumeric():
        destination, source, length = [int(num) for num in transfer.split()]
        for i in range(len(megaseeds)):
            pair = megaseeds.pop(0)
            begin = pair[0]
            end = pair[1]
            if source <= begin < source + length and source <= end < source + length:
                temp.append([destination + begin - source, destination + end - source])
            elif source <= begin < source+length:
                temp.append([destination + begin - source, destination + length - 1])
                megaseeds.append([source+length, end])
            elif source <= end < source + length:
                temp.append([destination, destination + end - source])
                megaseeds.append([begin, source])
            else:
                megaseeds.append([begin, end])
    else:
        for seed in temp:
            megaseeds.append(seed)
        temp = []
for seed in temp:
    megaseeds.append(seed)

print(min(megaseeds))
print(megaseeds.pop(megaseeds.index(min(megaseeds))))
print('answer part 2', min(megaseeds))