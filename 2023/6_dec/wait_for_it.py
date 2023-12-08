with open("input.txt") as f:
    info = f.read().splitlines()

info = [line.split() for line in info]


def race(time, distance):
    wins = 0
    for i in range(0, time+1):
        if i * (time - i) > distance:
            wins += 1
    return wins

score = 1
for i in range(1, len(info[0])):
    score *= race(int(info[0][i]), int(info[1][i]))

print('answer part 1', score)

time = ''.join(info[0][1:])
distance = ''.join(info[1][1:])

print(time, distance)
print('answer part 2', race(int(time), int(distance)))
