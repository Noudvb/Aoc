with open("input.txt") as f:
    info = f.read().splitlines()

info = [line.split(',') for line in info]


def dehash(step):
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


sum = 0
for step in info[0]:
    sum += dehash(step)
print('answer to part 1:', sum)

boxes = [{} for _ in range(256)]
for step in info[0]:
    if step[-1] == '-':
        box = dehash(step[:-1])
        boxes[box].pop(step[:-1], None)
    else:
        box = dehash(step[:-2])
        boxes[box][step[:-2]] = int(step[-1])

power = 0
for index_box, box in enumerate(boxes):
    for index_slot, value in enumerate(box.values()):
        power += (index_box +1) * (index_slot+1) * value

print('answer to part 2:', power)