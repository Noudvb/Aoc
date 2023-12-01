import numpy as np

with (open("input.txt") as f):
    info = f.read().splitlines()

original_map = [[int(point) for point in line] for line in info]
map = np.pad(original_map, pad_width=1, mode='constant', constant_values=10)

lowpoints = []
lowpoints_locations = []
for i in range(1, len(map)-1):
    for j in range(1, len(map[0])-1):
        if (map[i-1][j] > map[i][j]
                and map[i+1][j] > map[i][j]
                and map[i][j-1] > map[i][j]
                and map[i][j+1] > map[i][j]):
            lowpoints.append(map[i][j])
            lowpoints_locations.append([i, j])

print("lowpoints:", sum(lowpoints)+len(lowpoints))

schadow = np.zeros((len(map), len(map[0])))
def basin(i, j):
    total = 1
    if 9 > map[i-1][j] > map[i][j] and schadow[i-1][j] == 0:
        schadow[i - 1][j] = 1
        total += basin(i-1, j)
    if 9 > map[i+1][j] > map[i][j] and schadow[i+1][j] == 0:
        schadow[i + 1][j] = 1
        total += basin(i+1, j)
    if 9 > map[i][j-1] > map[i][j] and schadow[i][j-1] == 0:
        schadow[i][j - 1] = 1
        total += basin(i, j-1)
    if 9 > map[i][j+1] > map[i][j] and schadow[i][j+1] == 0:
        schadow[i][j + 1] = 1
        total += basin(i, j+1)
    return total


basins = []
for point in lowpoints_locations:
    basins.append(basin(point[0], point[1]))
basins.sort(reverse=True)
print("basins:", basins[0]*basins[1]*basins[2])
