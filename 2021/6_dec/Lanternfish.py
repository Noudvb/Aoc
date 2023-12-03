import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

fishes = [int(fish) for fish in info[0].split(",")]

count = np.zeros(9)
for fish in info[0].split(","):
    count[int(fish)] += 1

for day in range(256):
    new_fish = count[0]
    count = np.delete(count, 0)
    count[6] += new_fish
    count = np.append(count, new_fish)

print(sum(count))