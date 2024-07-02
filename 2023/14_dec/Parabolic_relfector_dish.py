import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

grid1 = np.array([[char for char in line] for line in info])


def roll_up(grid):
    cor = np.where(grid == 'O')
    for i in range(len(cor[0])):
        y, x = cor[0][i], cor[1][i]
        for j in range(y-1, -1, -1):
            if grid[j, x] == '.':
                grid[j, x] = 'O'
                grid[j+1, x] = '.'
            else:
                break
    return grid


def cal_load(grid):
    load = 0
    for index, line in enumerate(np.flip(grid, axis=0)):
        load += (index + 1) * np.count_nonzero(line == 'O')
    return load


grid1 = roll_up(grid1)
print('answer to part 1:', cal_load(grid1))

grid2 = np.array([[char for char in line] for line in info])

grid2 = np.rot90(grid2, 1)
loads = []
cycle = 0
grids = []
while True:
    cycle += 1
    for j in range(4):
        grid2 = roll_up(np.rot90(grid2, -1))

    if grid2.tobytes() in grids:
        repeat2 = cycle - grids.index(grid2.tobytes())-1
        answer = (1000000000 - cycle) % repeat2
        print('answer to part 2:', loads[-(repeat2 - answer)])
        break

    loads.append(cal_load(np.rot90(grid2, -1)))
    grids.append(grid2.tobytes())
