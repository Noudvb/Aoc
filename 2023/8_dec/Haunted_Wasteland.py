import numpy as np
import sympy as sp

with open("input.txt") as f:
    info = f.read().splitlines()

directions = [1 if char == 'R' else 0 for char in info[0]]
sequence = [step.split(' = ') for step in info[2:]]

seqdict = {}
for step in sequence:
    seqdict[step[0]] = step[1][1:-1].split(', ')

location = 'AAA'
i = 0
while location != 'ZZZ':
    location = seqdict[location][directions[i % len(directions)]]
    i += 1

print('answer part 1:', i)

locations = []
for pair in sequence:
    if pair[0][2] == 'A':
        locations.append(pair[0])

steps = []
for j, location in enumerate(locations):
    i = 0
    temp_location = location
    while temp_location[-1] != 'Z':
        temp_location = seqdict[temp_location][directions[i % len(directions)]]
        i += 1
    steps.append(i)

print('answer to part 2:', sp.lcm(steps))