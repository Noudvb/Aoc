import numpy as np

with open("Input.txt") as f:
    info = f.read().split()


map = np.array([[char for char in line] for line in info])
grid = np.zeros((len(map), len(map[0])))
turn = np.array([[0, 1], [-1, 0]])
start_heading = np.array([0, -1])

for row_idx, row in enumerate(map):
    for col_idx, char in enumerate(row):
        if char == "^":
            start_x, start_y = col_idx, row_idx

heading = start_heading
loc_x, loc_y = start_x, start_y
grid[loc_y][loc_x] = 1
while 0 <= loc_x + heading[0] < len(map) and 0 <= loc_y + heading[1] < len(map[0]):
    while map[loc_y + heading[1]][loc_x + heading[0]] == "#":
        heading = heading @ turn
    loc_x += heading[0]
    loc_y += heading[1]
    grid[loc_y][loc_x] = 1


print("Part 1: ", np.count_nonzero(grid))


def detect_loop(map, start_x, start_y):
    heading = np.array([0, -1])
    turn = np.array([[0, 1], [-1, 0]])
    visited = set()
    loc_x, loc_y = start_x, start_y

    while 0 <= loc_x + heading[0] < len(map) and 0 <= loc_y + heading[1] < len(map[0]):
        state = (loc_x, loc_y, tuple(heading))
        if state in visited:
            return True
        visited.add(state)

        while map[loc_y + heading[1]][loc_x + heading[0]] == "#":
            heading = heading @ turn
        loc_x += heading[0]
        loc_y += heading[1]
    return False


loops = 0
for i in range(len(map)):
    print("starting row: ", i)
    for j in range(len(map[0])):
        if grid[i][j] == 1 and map[i][j] == ".":
            map[i][j] = "#"
            if detect_loop(map, start_x, start_y):
                loops += 1
            map[i][j] = "."

print("Part 2:", loops)
