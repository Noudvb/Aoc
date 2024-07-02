with open("input.txt") as f:
    info = f.read().splitlines()

flipflop = []
con = []
queue = []
for line in info:
    if line[0] == '%':
        flipflop.append(line.split(' -> ')[0][1:])
    elif line[0] == '&':
        con.append(line.split(' -> ')[0][1:])
    else:
        for item in line.split(' -> ')[1].split(', '):
            queue.append([item, 'low'])

print(queue)
print(flipflop, con)
