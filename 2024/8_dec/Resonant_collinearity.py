import numpy as np
from collections import defaultdict
from math import gcd

with open("Input.txt") as f:
    info = f.read().split()


def calculate_points(val1, val2):
    diff = val2 - val1
    p1 = val1 - diff
    p2 = val2 + diff
    return p1, p2


def calculate_points2(val1, val2, chart):
    diff = val2 - val1
    commondif = gcd(diff[0], diff[1])
    diff = diff//commondif
    points = []
    points.append(val1)
    p = val1 - diff

    while np.all((0 <= p) & (p < np.array([len(chart), len(chart[0])]))):
        points.append(p)
        p = p - diff

    p = val1 + diff
    while np.all((0 <= p) & (p < np.array([len(chart), len(chart[0])]))):
        points.append(p)
        p = p + diff

    return points


chart = np.array([[char for char in line]for line in info])
grid = np.zeros((len(chart), len(chart[0])))
antennas = defaultdict(list)

for i, line in enumerate(chart):
    for j, char in enumerate(line):
        if char != ".":
            antennas[char].append(np.array([i, j]))

for key, values in antennas.items():
    for k, cor1 in enumerate(values):
        for cor2 in values[k+1:]:
            p1, p2 = calculate_points(cor1, cor2)
            if np.all((0 <= p1) & (p1 < np.array([len(chart), len(chart[0])]))):
                grid[p1[0], p1[1]] = 1
            if np.all((0 <= p2) & (p2 < np.array([len(chart), len(chart[0])]))):
                grid[p2[0], p2[1]] = 1

print("Part 1:", np.count_nonzero(grid))

for key, values in antennas.items():
    for k, cor1 in enumerate(values):
        for cor2 in values[k+1:]:
            points = calculate_points2(cor1, cor2, chart)
            for p in points:
                if np.all((0 <= p) & (p < np.array([len(chart), len(chart[0])]))):
                    grid[p[0], p[1]] = 1

print("Part 2:", np.count_nonzero(grid))
