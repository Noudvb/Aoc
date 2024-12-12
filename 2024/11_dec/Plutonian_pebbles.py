from collections import Counter


def blink(seq, times):
    for i in range(times):
        temp_seq = Counter()
        for num, amount in seq.items():
            if num == 0:
                temp_seq[1] += amount
            elif len(str(num)) % 2 == 0:
                half = int(len(str(num)) / 2)
                temp_seq[int(str(num)[:half])] += amount
                temp_seq[int(str(num)[half:])] += amount
            else:
                temp_seq[num * 2024] += amount
        seq = temp_seq
    return seq


with open("Input.txt") as f:
    info = f.read().split()

seq = Counter([int(item) for item in info])

print("Part 1: ", sum(blink(seq, 25).values()))
print("Part 2: ", sum(blink(seq, 75).values()))

