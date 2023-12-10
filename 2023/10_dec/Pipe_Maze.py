import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

grid = [[char for char in line] for line in info]
start = [[index, row.index('S'), 'S'] for index, row in enumerate(grid) if 'S' in row]
pipes = np.zeros(np.shape(grid))
pipes[start[0][0]][start[0][1]] = 1
route = start.copy()

prev_y, prev_x = -1, -1
run = True
while run:
    curr_y, curr_x, path = route[-1][0:3]
    if path in ['|', 'F', '7', 'S'] and curr_y + 1 != prev_y:
        route.append([curr_y + 1, curr_x, grid[curr_y + 1][curr_x], 'south'])
        pipes[curr_y + 1][curr_x] = 8
    elif path in ['|', 'L', 'J', 'S'] and curr_y - 1 != prev_y:
        route.append([curr_y - 1, curr_x, grid[curr_y - 1][curr_x], 'north'])
        pipes[curr_y - 1][curr_x] = 8
    elif path in ['-', 'F', 'L', 'S'] and curr_x + 1 != prev_x:
        route.append([curr_y, curr_x + 1, grid[curr_y][curr_x + 1], 'east'])
        pipes[curr_y][curr_x + 1] = 8
    elif path in ['-', 'J', '7', 'S'] and curr_x - 1 != prev_x:
        route.append([curr_y, curr_x - 1, grid[curr_y][curr_x - 1], 'west'])
        pipes[curr_y][curr_x - 1] = 8

    prev_y, prev_x, path = route[-2][0:3]
    if 'S' in route[-1]:
        run = False

print('answer part 1:', int((len(route) - 1)/2))

Lenclosed = np.zeros(np.shape(grid))
Renclosed = np.zeros(np.shape(grid))
R = True
L = True
for step in route:
    if step[-1] == 'south':
        if step[1]+1 >= len(pipes[0]):
            L = False
        elif pipes[step[0]][step[1]+1] == 0:
            Lenclosed[step[0]][step[1]+1] = 1
        if step[2] == 'J' and step[0] + 1 < len(pipes) and pipes[step[0]+1][step[1]] == 0:
            Lenclosed[step[0] + 1][step[1]] = 1

        if step[1]-1 < 0:
            R = False
        elif pipes[step[0]][step[1]-1] == 0:
            Renclosed[step[0]][step[1]-1] = 1
        if step[2] == 'L' and step[0] + 1 < len(pipes) and pipes[step[0]+1][step[1]] == 0:
            Renclosed[step[0] + 1][step[1]] = 1

    elif step[-1] == 'north':
        if step[1]-1 < 0:
            L = False
        elif pipes[step[0]][step[1]-1] == 0:
            Lenclosed[step[0]][step[1]-1] = 1
        if step[2] == 'F' and step[0]-1 >= 0 and pipes[step[0]-1][step[1]] == 0:
            Lenclosed[step[0]-1][step[1]] = 1

        if step[1]+1 >= len(pipes[0]):
            R = False
        elif pipes[step[0]][step[1]+1] == 0:
            Renclosed[step[0]][step[1]+1] = 1
        if step[2] == '7' and step[0]-1 >= 0 and pipes[step[0]-1][step[1]] == 0:
            Renclosed[step[0]-1][step[1]] = 1

    elif step[-1] == 'east':
        if step[0]-1 < 0:
            L = False
        elif pipes[step[0]-1][step[1]] == 0:
            Lenclosed[step[0]-1][step[1]] = 1
        if step[2] == '7' and step[1]+1 < len(pipes[0]) and pipes[step[0]][step[1]+1] == 0:
            Lenclosed[step[0]][step[1]+1] = 1

        if step[0]+1 >= len(pipes):
            R = False
        elif pipes[step[0]+1][step[1]] == 0:
            Renclosed[step[0]+1][step[1]] = 1
        if step[2] == 'J' and step[1]+1 < len(pipes[0]) and pipes[step[0]][step[1]+1] == 0:
            Renclosed[step[0]][step[1]+1] = 1

    elif step[-1] == 'west':
        if step[0]+1 >= len(pipes):
            L = False
        elif pipes[step[0]+1][step[1]] == 0:
            Lenclosed[step[0]+1][step[1]] = 1
        if step[2] == 'L' and step[1]-1 >= 0 and pipes[step[0]][step[1]-1] == 0:
            Lenclosed[step[0]][step[1]-1] = 1

        if step[0]-1 < 0:
            R = False
        elif pipes[step[0]-1][step[1]] == 0:
            Renclosed[step[0]-1][step[1]] = 1
        if step[2] == 'F' and step[1]-1 >= 0 and pipes[step[0]][step[1]-1] == 0:
            Renclosed[step[0]][step[1]-1] = 1

if L and list(Lenclosed[0]).count(1) == 0:
    enclosed = Lenclosed.copy() + pipes
if R and list(Renclosed[0]).count(1) == 0:
    enclosed = Renclosed.copy() + pipes

for i in range(len(enclosed)):
    for j in range(len(enclosed[0])):
        if enclosed[i][j] == 0 and (enclosed[i-1][j] == 1 or enclosed[i][j-1] == 1):
            enclosed[i][j] = 1

print('answer part 2:', np.count_nonzero(enclosed == 1))
