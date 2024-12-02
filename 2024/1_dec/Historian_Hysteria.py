with open("Input.txt") as f:
    info = f.read().split()

left = []
right = []
for i in range(0, len(info), 2):
    left.append(int(info[i]))
    right.append(int(info[i+1]))

left.sort()
right.sort()

distance = 0
for i in range(len(left)):
    distance += abs(left[i]-right[i])

print("Part 1: ", distance)

similarity = 0
for i in range(len(left)):
    similarity += right.count(left[i])*left[i]

print("Part 2: ", similarity)