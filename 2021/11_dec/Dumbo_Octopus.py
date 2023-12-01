import numpy as np

with (open("input.txt") as f):
    info = f.read().splitlines()

map = np.array([[int(point) for point in line] for line in info])

height = len(map)
width = len(map[0])
ones = np.ones((width, height))


def add_neighbours(i, j):
    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if 0 <= y < height and 0 <= x < width and flash_map[y][x] == 0:
                map[y][x] += 1


flash_count = 0
for k in range(300):
    map = map + ones
    flash_map = np.zeros((width, height))
    while np.count_nonzero(map >= 10) > 0:
        for i in range(height):
            for j in range(width):
                if map[i][j] >= 10 and flash_map[i][j] == 0:
                    flash_map[i][j] = 1
                    map[i][j] = 0
                    add_neighbours(i, j)
    flash_count += np.count_nonzero(flash_map == 1)
    if height*width == np.count_nonzero(flash_map == 1):
        print(k+1, "mega flash")

print(flash_count)