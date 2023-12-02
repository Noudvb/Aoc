with open("input.txt") as f:
    info = f.read().splitlines()

info = [line.split(" ") for line in info]

depth = 0
position = 0
for step in info:
    if step[0] == 'forward':
        position += int(step[1])
    elif step[0] == 'down':
        depth += int(step[1])
    elif step[0] == 'up':
        depth -= int(step[1])

print('depth:', depth, '\nposition', position, '\nvalue:', depth*position)

depth = 0
position = 0
aim = 0
for step in info:
    if step[0] == 'forward':
        position += int(step[1])
        depth += aim*int(step[1])
    elif step[0] == 'down':
        aim += int(step[1])
    elif step[0] == 'up':
        aim -= int(step[1])

print('depth:', depth, '\nposition', position, '\nvalue:', depth*position)

