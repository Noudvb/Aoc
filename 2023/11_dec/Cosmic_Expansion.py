import numpy as np


def get_points(grid):
    points = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                points.append([i, j])
    return points


def get_distance(points):
    distance = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    return distance


with open("input.txt") as f:
    info = f.read().splitlines()

grid = [[point for point in line] for line in info]

insertions_rows = []
for i, row in enumerate(grid):
    if row.count('#') == 0:
        insertions_rows.append(i)

insertions_column = []
for i in range(len(grid[0])):
    if np.count_nonzero(np.array(grid)[:, i] == '#') == 0:
        insertions_column.append(i)

for index, value in enumerate(insertions_rows):
    grid.insert(value+index, list(np.zeros(len(grid[0]))))

for i, column in enumerate(insertions_column):
    for j in range(len(grid)):
        grid[j].insert(i+column, '.')

points = get_points(grid)
print('answer part 1:', get_distance(points))

longdistance = 0
points = get_points([[point for point in line] for line in info])
for i in range(len(points)):
    for j in range(i+1, len(points)):
        longdistance += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        for column in insertions_column:
            if points[i][1] <= column <= points[j][1] or points[j][1] <= column <= points[i][1]:
                longdistance += 999999
        for row in insertions_rows:
            if points[i][0] <= row <= points[j][0] or points[j][0] <= row <= points[i][0]:
                longdistance += 999999

print('answer part 2:', longdistance)
