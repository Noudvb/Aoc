import numpy as np
import re
from colorama import Fore, Style
import random

with open("Input.txt") as f:
    info = f.read().splitlines()

puzzle = []
for line in info:
    puzzle.append([int(num) for num in re.findall(r'-?\d+', line)])
width = 101  # 101
height = 103  # 103

grid = np.zeros((height, width))
for robot in puzzle:
    x, y, vx, vy = robot
    grid[(y + 100*vy) % height][(x + 100*vx) % width] += 1


mid_row, mid_col = height // 2, width // 2

top_left = grid[:mid_row, :mid_col]
top_right = grid[:mid_row, mid_col + 1:]
bottom_left = grid[mid_row + 1:, :mid_col]
bottom_right = grid[mid_row + 1:, mid_col + 1:]

print("Part 1:", np.sum(top_left) * np.sum(top_right) * np.sum(bottom_left) * np.sum(bottom_right))

i = 0
while True:
    grid = np.zeros((height, width))
    for robot in puzzle:
        x, y, vx, vy = robot
        grid[(y + i * vy) % height][(x + i * vx) % width] += 1
    if np.isin(grid, [0, 1]).all():
        print("Part 2: ", i)
        break

    i += 1

colors = [Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]


def is_connected(grid, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            return True
    return False


def print_christmas_tree(grid):
    for row in range(len(grid)):
        formatted_row = ""
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if is_connected(grid, row, col):
                    formatted_row += Fore.GREEN + "*" + Style.RESET_ALL  # Green for connected stars
                else:
                    formatted_row += random.choice(colors) + "*" + Style.RESET_ALL  # Random color for isolated stars
            else:
                formatted_row += " "  # Empty space
        print(formatted_row)

print_christmas_tree(grid)
