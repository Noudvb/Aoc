from collections import deque, Counter
import numpy as np
from itertools import product


def create_heatmap(grid, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path_length = queue.popleft()
        if (x, y) == end:
            grid[x][y] = int(path_length)
            return grid
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path_length + 1))
                grid[x][y] = int(path_length)
    return -1

with open("Input.txt") as f:
    info = f.read().splitlines()

grid = np.array([[char for char in line] for line in info], dtype=object)
start = tuple(np.argwhere(grid == 'S')[0])
end = tuple(np.argwhere(grid == 'E')[0])
heatmap = create_heatmap(grid, start, end)

shortcuts = []
for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        options = [(-1, 0, 1, 0), (0, -1, 0, 1), (-1, 0, 0, -1), (-1, 0, 0, 1), (1, 0, 0, -1), (1, 0, 0, 1)]
        for dy1, dx1, dy2, dx2 in options:
            if grid[y + dy1][x + dx1] != "#" and grid[y][x] == '#' and grid[y + dy2][x + dx2] != '#':
                shortcuts.append(abs(heatmap[y + dy2][x + dx2] - heatmap[y + dy1][x + dx1])-2)

part1 = 0
for key, value in sorted(Counter(shortcuts).items()):
    # print(f"There are {value} cheats that save {key} picoseconds.")
    if key >= 100:
        part1 += value

print("Part 1: ", part1)

counter = 0
height, width = grid.shape
maxjump = 20
min_cheat = 100

for x in range(height):
    for y in range(width):
        if grid[x, y] != "#":
            for dx, dy in product(range(-maxjump, maxjump + 1), repeat=2):
                steps = abs(dx) + abs(dy)
                if dx == dy == 0 or steps > maxjump:
                    continue
                addx, addy = x + dx, y + dy
                if 0 <= addx < height and 0 <= addy < width and isinstance(heatmap[addx][addy], int):
                    max_diff = heatmap[addx, addy] - heatmap[x, y] - steps
                    if max_diff >= min_cheat:
                        counter += 1

print("Part 2: ", counter)