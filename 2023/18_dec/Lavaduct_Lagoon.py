import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

steps = [line.split(' ') for line in info]
width, height = 0, 0

for step in steps:
    if step[0] == 'R':
        width += int(step[1])
    if step[0] == 'L':
        height += int(step[1])

grid = np.zeros((width*2, height*2))
position = (width, height)
grid[position] = 1
direction = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }


for step in steps:
    for i in range(1, int(step[1])+1):
        position = tuple(np.sum((position, direction[step[0]]), axis=0))
        grid[position] = 1


print(grid)

fill = False
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i, j] == 1:
            fill = True 
 

        if grid[i, j-1] == 1 and grid[i-1, j] == 1 and grid[i, j] == 0:
            grid[i, j] = 1
            if j+1 < len(grid[0]) and grid[i, j+1] == 1:
                break

print(np.count_nonzero(grid == 1))


# result = {
#     0: [0, 0]
# }
# y = 0
# for step in steps:
#     if step[0] == 'R':
#         result[y] = [result[y][0], int(step[1])]
#     elif step[0] == 'L':
#         result[y] = [int(step[1]), result[y][1]]
#     elif step[0] == 'U':
#         for i in range(int(step[1])):
#