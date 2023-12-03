import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

info = [[int(char) if char.isnumeric() else char for char in line] for line in info]


def check_part(grid, begin, end, row, gears, gears_score, num):
    part = False
    for i in range(row-1, row+2):
        for j in range(begin-1, end+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] != "." and isinstance(grid[i][j], int) is False:
                    part = True
                if grid[i][j] == "*":
                    gears[i][j] += 1
                    gears_score[i][j] *= num
    return part, gears, gears_score

gears = np.zeros((len(info), len(info[0])))
gears_score = np.ones((len(info), len(info[0])))
parts = []
for i in range(len(info)):
    begin = -1
    end = -1
    row = i
    num = ""
    for j in range(len(info[0])):
        if isinstance(info[i][j], int) and begin == -1:
            begin = j
            end = j
            num += str(info[i][j])
        elif isinstance(info[i][j], int):
            end = j
            num += str(info[i][j])
        elif begin != -1:
            part, gears, gears_score = check_part(info, begin, end, row, gears, gears_score, int(num))
            if part:
                parts.append(int(num))
            begin = -1
            end = -1
            num = ""
        if j == len(info[0])-1 and num.isnumeric():
            part, gears, gears_score = check_part(info, begin, end, row, gears, gears_score, int(num))
            if part:
                parts.append(int(num))
            begin = -1
            end = -1
            num = ""

print(sum(parts))

score = 0
for i in range(len(info)):
    for j in range(len(info[0])):
        if gears[i][j] == 2:
            score += gears_score[i][j]

print(score)
print(np.count_nonzero(gears > 2))

# 292446 to low