import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

grid = [[int(num) for num in line] for line in info]


def search(grid, route):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                continue
            else:
                route[i][j] = min(
                    route[max(i - 1, 0)][j],
                    route[i][max(j - 1, 0)],
                    route[min(i + 1, len(grid)-1)][j],
                    route[i][min(j + 1, len(grid)-1)]) + grid[i][j]
    return route


route = np.full((len(grid), len(grid[0])), np.inf)
route[0][0] = 0
print(" shortest path part 1: ", search(grid, route)[-1][-1])


ones = np.ones((len(grid), len(grid[0])))
original_grid = grid.copy()
rows = []
for i in range(5):
    row_grid = original_grid + ones * i
    for j in range(1, 5):
        row_grid = np.concatenate((row_grid, original_grid+ones*(i+j)), axis=1)
    rows.append(row_grid)

megagrid = rows[0]
for i in range(1, len(rows)):
    megagrid = np.concatenate((megagrid, rows[i]), axis = 0)

for i in range(len(megagrid)):
    for j in range(len(megagrid)):
        if megagrid[i][j] > 9:
            megagrid[i][j] -= 9

route = np.full((len(megagrid), len(megagrid[0])), np.inf)
route[0][0] = 0
paths = []
for i in range(10):
    route = search(megagrid, route)
    paths.append(route[-1][-1])

result = route
print(" shortest path part 2: ", result[-1][-1])
