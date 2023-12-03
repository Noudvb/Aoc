import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

start = [int(pos) for pos in info[0].split(",")]

aim = np.median(start)

fuel = 0
for start_pos in start:
    fuel += abs(start_pos-aim)

print(fuel)

aim2 = round(np.mean(start))
print(aim2)
fuel2 = 0
for start_pos in start:
    steps = abs(start_pos-aim2)
    fuel2 += steps*(steps+1) * 0.5

print(fuel2)

fuel3 = []
for i in range(max(start)):
    fueltemp = 0
    for start_pos in start:
        steps = abs(start_pos - i)
        fueltemp += steps * (steps + 1) * 0.5
    fuel3.append(fueltemp)

print(min(fuel3), fuel3.index(min(fuel3)))