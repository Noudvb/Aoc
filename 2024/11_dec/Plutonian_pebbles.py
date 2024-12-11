from collections import Counter

with open("Input.txt") as f:
    info = f.read().split()

seq = Counter([int(item) for item in info])


for i in range(75):
    temp_seq = Counter()
    for num, amount in seq.items():
        if num == 0:
            temp_seq[1] += amount
        elif len(str(num))%2 == 0:
            half = int(len(str(num))/2)
            temp_seq[int(str(num)[:half])] += amount
            temp_seq[int(str(num)[half:])] += amount
        else:
            temp_seq[num*2024] += amount
    seq = temp_seq

print("Part 1: ", sum(seq.values()))

