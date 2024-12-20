import numpy as np
from collections import deque


def shortest_path(grid, start, goal):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1

with open("Input.txt") as f:
    info = f.read().splitlines()

cord = [[int(char) for char in line.split(",")] for line in info]
width = 71
height = 71

grid = np.zeros((width, height))

for i, cor in enumerate(cord):
    if i == 1024:
        print("Part 1:", shortest_path(grid, (0, 0), (width - 1, height - 1)))
    grid[cor[1]][cor[0]] = 1
    if shortest_path(grid, (0, 0), (width - 1, height - 1)) == - 1:
        print("Part 2:", cor)
        break


