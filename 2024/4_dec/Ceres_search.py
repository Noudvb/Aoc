with open("Input.txt") as f:
    info = f.read().split()

grid = []
for line in info:
    grid.append([char for char in line])

count1 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "X":
            result = [0] * 8
            for index, k in enumerate(["X", "M", "A", "S"]):
                if i - index >= 0 and grid[i-index][j] == k:
                    result[0] += 1
                if i + index < len(grid) and grid[i+index][j] == k:
                    result[1] += 1
                if j - index >= 0 and grid[i][j-index] == k:
                    result[2] += 1
                if j + index < len(grid[0]) and grid[i][j+index] == k:
                    result[3] += 1

                if i - index >= 0 and j - index >= 0 and grid[i-index][j-index] == k:
                    result[4] += 1
                if i + index < len(grid) and j - index >= 0 and grid[i+index][j-index] == k:
                    result[5] += 1
                if i + index < len(grid) and j + index < len(grid[0]) and grid[i+index][j+index] == k:
                    result[6] += 1
                if i - index >= 0 and j + index < len(grid[0]) and grid[i-index][j+index] == k:
                    result[7] += 1
            count1 += result.count(4)

print("Part 1: ", count1)

count2 = 0
for i in range(len(grid)-2):
    for j in range(len(grid[0])-2):
        if grid[i][j] == "M" and grid[i][j+2] == "M" and grid[i+1][j+1] == "A" and grid[i+2][j] == "S" and grid[i+2][j+2] == "S":
            count2 += 1
        if grid[i][j] == "M" and grid[i][j + 2] == "S" and grid[i + 1][j + 1] == "A" and grid[i + 2][j] == "M" and grid[i + 2][j + 2] == "S":
            count2 += 1
        if grid[i][j] == "S" and grid[i][j + 2] == "S" and grid[i + 1][j + 1] == "A" and grid[i + 2][j] == "M" and \
                grid[i + 2][j + 2] == "M":
            count2 += 1
        if grid[i][j] == "S" and grid[i][j+2] == "M" and grid[i+1][j+1] == "A" and grid[i+2][j] == "S" and grid[i+2][j+2] == "M":
            count2 += 1

print("Part 2: ", count2)
