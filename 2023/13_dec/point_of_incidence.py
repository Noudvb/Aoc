import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

grid = [[1 if char == '#' else 0 for char in line] for line in info]
grid.append([])

map = []
grids = []
for line in grid:
    if not line:
        grids.append(np.array(map))
        map = []
    else:
        map.append(line)


def vertical_mirror(plane):
    for i in range(1, len(plane[0]) // 2 + 1):
        if np.equal(plane[:, :i], np.flip(plane[:, i:i * 2], axis=1)).all():
            return i
        if np.equal(plane[:, -i:], np.flip(plane[:, -i * 2:-i], axis=1)).all():
            return len(plane[0]) - i
    return 0


def smudge_vertical_mirror(plane):
    for i in range(1, len(plane[0]) // 2 + 1):
        if np.count_nonzero(plane[:, :i] + np.flip(plane[:, i:i * 2], axis=1) == 1) == 1:
            return i
        if np.count_nonzero(plane[:, -i:] + np.flip(plane[:, -i * 2:-i], axis=1) == 1) == 1:
            return len(plane[0]) - i
    return 0


sum1 = 0
sum2 = 0
for grid in grids:
    sum1 += vertical_mirror(grid)
    sum1 += vertical_mirror(np.transpose(grid)) * 100

    sum2 += smudge_vertical_mirror(grid)
    sum2 += smudge_vertical_mirror(np.transpose(grid)) * 100

print('answer part 1:', sum1)
print('answer part 2:', sum2)
