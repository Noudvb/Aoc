import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

points = []
folds = []
maxx = 0
maxy = 0
for line in info:
    temp = line.split(',')
    if len(temp) > 1:
        points.append([int(cor) for cor in temp])
        maxx = max(maxx, int(temp[0]))
        maxy = max(maxy, int(temp[1]))
    elif temp[0] == "":
        continue
    else:
        fold = temp[0].split("=")
        folds.append([fold[0], int(fold[1])])

grid = np.zeros((maxy+1, maxx+1))
for point in points:
    grid[point[1]][point[0]] += 1


def fold(axis, grid, num):
    if axis == 'fold along y':
        grid = np.delete(grid, num, 0)
        grid1, grid2 = np.split(grid, 2, axis=0)
        return grid1 + np.flip(grid2, 0)
    elif axis == 'fold along x':
        grid = np.delete(grid, num, 1)
        grid1, grid2 = np.split(grid, 2, axis=1)
        return grid1 + np.flip(grid2, 1)


first = True
for vouw in folds:
    grid = fold(vouw[0], grid, vouw[1])
    if first:
        print("Dots after first fold:", np.count_nonzero(grid > 0))
        first = False

for line in grid:
    text = ""
    for char in line:
        if char > 0:
            text += "##"
        else:
            text += "  "
    print(text)


for row in grid:
    print("".join("■■■■" if cell > 0 else "    " for cell in row))
    print("".join("■■■■" if cell > 0 else "    " for cell in row))