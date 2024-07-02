import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()


grid = np.array([[point for point in line] for line in info])

def call_energized(start):
    path = [start]
    visited = []
    energized = np.zeros(np.shape(grid))
    direction = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }
    while path:
        step = path.pop(0)
        energized[step[1]] = 1
        if step in visited:
            pass
        elif (grid[step[1]] == '.'
                or (grid[step[1]] == '|' and (step[0] == 'S' or step[0] == 'N'))
                or (grid[step[1]] == '-' and (step[0] == 'E' or step[0] == 'W'))):
            next_cor = tuple(np.sum([step[1], direction[step[0]]], axis=0))
            if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                path.append([step[0], next_cor])
        elif grid[step[1]] == '/':
            if step[0] == 'N':
                next_cor = tuple(np.sum([step[1], (0, 1)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['E', next_cor])
            elif step[0] == 'E':
                next_cor = tuple(np.sum([step[1], (-1, 0)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['N', next_cor])
            elif step[0] == 'S':
                next_cor = tuple(np.sum([step[1], (0, -1)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['W', next_cor])
            elif step[0] == 'W':
                next_cor = tuple(np.sum([step[1], (1, 0)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['S', next_cor])
        elif grid[step[1]] == '\\':
            if step[0] == 'N':
                next_cor = tuple(np.sum([step[1], (0, -1)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['W', next_cor])
            elif step[0] == 'E':
                next_cor = tuple(np.sum([step[1], (1, 0)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['S', next_cor])
            elif step[0] == 'S':
                next_cor = tuple(np.sum([step[1], (0, 1)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['E', next_cor])
            elif step[0] == 'W':
                next_cor = tuple(np.sum([step[1], (-1, 0)], axis=0))
                if 0 <= next_cor[0] < len(grid[0]) and 0 <= next_cor[1] < len(grid):
                    path.append(['N', next_cor])
        elif grid[step[1]] == '|' and (step[0] == 'E' or step[0] == 'W'):
            next_cor1 = tuple(np.sum([step[1], (-1, 0)], axis=0))
            next_cor2 = tuple(np.sum([step[1], (1, 0)], axis=0))
            if 0 <= next_cor1[0] < len(grid[0]) and 0 <= next_cor1[1] < len(grid):
                path.append(['N', next_cor1])
            if 0 <= next_cor2[0] < len(grid[0]) and 0 <= next_cor2[1] < len(grid):
                path.append(['S', next_cor2])
        elif grid[step[1]] == '-' and (step[0] == 'S' or step[0] == 'N'):
            next_cor1 = tuple(np.sum([step[1], (0, -1)], axis=0))
            next_cor2 = tuple(np.sum([step[1], (0, 1)], axis=0))
            if 0 <= next_cor1[0] < len(grid[0]) and 0 <= next_cor1[1] < len(grid):
                path.append(['W', next_cor1])
            if 0 <= next_cor2[0] < len(grid[0]) and 0 <= next_cor2[1] < len(grid):
                path.append(['E', next_cor2])
        visited.append(step)
    return np.count_nonzero(energized != 0)


print('answer to part 1:', call_energized(['E', (0, 0)]))

energie = []
for i in range(110):
    energie.append(call_energized(['S', (0, i)]))
    energie.append(call_energized(['N', (109, i)]))
    energie.append(call_energized(['E', (i, 0)]))
    energie.append(call_energized(['W', (i, 109)]))
    print(i)
print(max(energie))