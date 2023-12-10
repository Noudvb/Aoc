with open("input.txt") as f:
    sequences = f.read().splitlines()

sequences = [[int(numb) for numb in sequence.split()] for sequence in sequences]

sum_next = 0
sum_prev = 0
for index, sequence in enumerate(sequences):
    triangle = [sequence]
    while triangle[-1][-1] != 0:
        temp = []
        for i in range(len(triangle[-1])-1):
            temp.append(triangle[-1][i+1] - triangle[-1][i])
        triangle.append(temp)
    triangle[-1].append(0)
    for j in range(2, len(triangle)+1):
        triangle[-j].append(triangle[-j][-1] + triangle[-j+1][-1])
        triangle[-j].insert(0, triangle[-j][0] - triangle[-j+1][0])
    sequences[index] = triangle[0]
    sum_next += triangle[0][-1]
    sum_prev += triangle[0][0]

print('answer part 1:', sum_next)
print('answer part 2:', sum_prev)