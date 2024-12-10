import numpy as np

with open("Input.txt") as f:
    info = f.read().splitlines()

disk = [int(n) for n in info[0]]

Id = 0
sequencelst = []
for index, item in enumerate(disk):
    if index % 2 == 0:
        sequencelst.extend([Id] * item)
        Id += 1
    else:
        sequencelst.extend(["."] * item)

sequence = np.array(sequencelst, dtype=object)
points = np.where(sequence == ".")[0].tolist()
numbers = np.where(sequence != ".")[0].tolist()

while points[0] <= numbers[-1]:
    sequence[points[0]] = sequence[numbers[-1]]
    sequence[numbers[-1]] = "."
    points.pop(0)
    numbers.pop(-1)

sum1 = sum(index * int(item) for index, item in enumerate(sequence) if item != ".")

print("Part 1:", sum1)



sequence = np.array(sequencelst, dtype=object)
max_id = Id - 1
free_space_blocks = []
current_start = None

for i, value in enumerate(sequence):
    if value == ".":
        if current_start is None:
            current_start = i
    else:
        if current_start is not None:
            free_space_blocks.append((current_start, i - current_start))
            current_start = None
if current_start is not None:
    free_space_blocks.append((current_start, len(sequence) - current_start))

for file_id in range(max_id, -1, -1):
    file_positions = np.where(sequence == file_id)[0]
    if not len(file_positions):
        continue
    file_size = len(file_positions)

    for i, (start, size) in enumerate(free_space_blocks):
        if size >= file_size and start < file_positions[0]:
            sequence[start:start + file_size] = file_id
            sequence[file_positions] = "."

            del free_space_blocks[i]
            if start + file_size < start + size:
                free_space_blocks.insert(i, (start + file_size, size - file_size))
            break

total_sum = sum(index * item for index, item in enumerate(sequence) if item != ".")

print("Part 2:", total_sum)


