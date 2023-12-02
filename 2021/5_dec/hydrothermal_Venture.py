import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

info = [[[int(point) for point in cor.split(",")] for cor in step.split(" -> ")] for step in info]

max_x = 0
max_y = 0
for step in info:
    for point in step:
        max_x = max(point[0], max_x)
        max_y = max(point[0], max_y)

grid = np.zeros((max_x+1, max_y+1))
for step in info:
    minx = min(step[0][0], step[1][0])
    maxx = max(step[0][0], step[1][0])
    miny = min(step[0][1], step[1][1])
    maxy = max(step[0][1], step[1][1])
    if minx == maxx or miny == maxy:
        for i in range(minx, maxx+1):
            for j in range(miny, maxy+1):
                grid[j][i] += 1
    else:
        x_step = 1
        y_step = 1
        if step[0][0] > step[1][0]:
            x_step = -1
        if step[0][1] > step[1][1]:
            y_step = -1
        for i in range(abs(step[0][0] - step[1][0]) + 1):
            grid[step[0][1] + y_step * i][step[0][0] + x_step * i] += 1

print(grid)
print(np.count_nonzero(grid >= 2))