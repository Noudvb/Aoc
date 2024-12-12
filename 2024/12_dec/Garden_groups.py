import numpy as np

with open("Input.txt") as f:
    info = f.read().split()

region = np.array([[char for char in line] for line in info])
grid = np.zeros(region.shape)


def find_gardens(map, x, y, value, grid):
    stack = [(x, y)]
    area = 0
    border = 0
    area_map = set()

    while stack:
        cx, cy = stack.pop()

        if grid[cy][cx] == 1:
            continue

        grid[cy][cx] = 1
        area += 1
        area_map.add((cx, cy))

        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
                if map[ny][nx] == value and grid[ny][nx] == 0:
                    stack.append((nx, ny))
                elif map[ny][nx] != value:
                    border += 1
            else:
                border += 1

    return np.array([area, border, area_map])


def find_corners(area_map):
    corners = 0
    for cor in area_map:
        for nx, ny in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            # Outside corners
            if ((cor[0] + ny, cor[1]) not in area_map and
                    (cor[0], cor[1] + nx) not in area_map):
                corners += 1
            # inside corners
            if ((cor[0] + ny, cor[1]) in area_map and
                    (cor[0], cor[1] + nx) in area_map and
                    (cor[0] + ny, cor[1] + nx) not in area_map):
                corners += 1
    return corners


totals = []
for y in range(len(region)):
    for x, value in enumerate(region[y]):
        if grid[y][x] == 0:
            totals.append(find_gardens(region, x, y, value, grid))

amount1 = 0
amount2 = 0
for item in totals:
    amount1 += item[0] * item[1]
    amount2 += item[0] * find_corners(item[2])

print("Part 1: ", amount1)
print("Part 2: ", amount2)
