import numpy as np


def move_robot(grid, robot_pos, moves):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    for move in moves:
        dr, dc = directions[move]
        new_r, new_c = robot_pos[0] + dr, robot_pos[1] + dc

        if grid[new_r][new_c] == '.':
            grid[robot_pos[0]][robot_pos[1]] = '.'
            grid[new_r][new_c] = '@'
            robot_pos = (new_r, new_c)

        elif grid[new_r][new_c] == 'O':
            boxes_to_push = [(new_r, new_c)]
            box_r, box_c = new_r + dr, new_c + dc

            while grid[box_r][box_c] == 'O':
                boxes_to_push.append((box_r, box_c))
                box_r, box_c = box_r + dr, box_c + dc

            if grid[box_r][box_c] == '.':
                grid[box_r][box_c] = 'O'
                grid[new_r][new_c] = '@'
                grid[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (new_r, new_c)

    return grid


def move_robot2(grid, robot_pos, moves):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    for move in moves:
        dr, dc = directions[move]
        new_r, new_c = robot_pos[0] + dr, robot_pos[1] + dc

        if grid[new_r][new_c] == '.':
            grid[robot_pos[0]][robot_pos[1]] = '.'
            grid[new_r][new_c] = '@'
            robot_pos = (new_r, new_c)

        elif grid[new_r][new_c] == '[' or grid[new_r][new_c] == ']':
            boxes_to_push = [(new_r, new_c)]
            box_r, box_c = new_r + dr, new_c + dc

            while grid[box_r][box_c] == '[' or grid[box_r][box_c] == ']':
                boxes_to_push.append((box_r, box_c))
                box_r, box_c = box_r + dr, box_c + dc

            if grid[box_r][box_c] == '.':
                grid[box_r][box_c] = 'O'
                grid[new_r][new_c] = '@'
                grid[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (new_r, new_c)

    return grid

def count_score(grid):
    score = 0
    for pos in np.argwhere(grid == 'O'):
        score += pos[0] * 100 + pos[1]
    return score

with open("Input.txt") as f:
    info = f.read().splitlines()

grid_list = []
moves = ""
directions = False
for line in info:
    if line == "":
        directions = True
    if not directions:
        grid_list.append([char for char in line])
    elif directions and line != "":
        moves += line

grid = np.array(grid_list)
pos = np.argwhere(grid == '@')[0]

grid = move_robot(grid, (pos[1], pos[0]), moves)

print("Part 1: ", count_score(grid))

