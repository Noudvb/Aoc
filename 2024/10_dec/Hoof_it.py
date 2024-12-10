import numpy as np

with open("Input.txt") as f:
    info = f.read().split()

map = np.array([[int(char) for char in line] for line in info])


def find_trail(map, x, y, value):
    count = set()
    if value == 9:
        return {(x, y)}

    if x+1 < len(map[0]) and map[y][x+1] == value + 1:
        count |= find_trail(map, x+1, y, map[y][x+1])
    if x-1 >= 0 and map[y][x-1] == value + 1:
        count |= find_trail(map, x-1, y, map[y][x-1])

    if y+1 < len(map) and map[y+1][x] == value + 1:
        count |= find_trail(map, x, y+1, map[y+1][x])
    if y-1 >= 0 and map[y-1][x] == value + 1:
        count |= find_trail(map, x, y-1, map[y-1][x])

    return count


def find_trail2(map, x, y, value):
    count = 0
    if value == 9:
        return 1

    if x+1 < len(map[0]) and map[y][x+1] == value + 1:
        count += find_trail2(map, x+1, y, map[y][x+1])
    if x-1 >= 0 and map[y][x-1] == value + 1:
        count += find_trail2(map, x-1, y, map[y][x-1])

    if y+1 < len(map) and map[y+1][x] == value + 1:
        count += find_trail2(map, x, y+1, map[y+1][x])
    if y-1 >= 0 and map[y-1][x] == value + 1:
        count += find_trail2(map, x, y-1, map[y-1][x])

    return count

total1 = 0
total2 = 0
for y in range(len(map)):
    for x, value in enumerate(map[y]):
        if value == 0:
            total1 += len(find_trail(map, x, y, value))
            total2 += find_trail2(map, x, y, value)

print("Part 1: ", total1)
print("Part 2: ", total2)
