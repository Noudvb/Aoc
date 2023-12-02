with open("input.txt") as f:
    info = f.read().splitlines()

info = [int(line) for line in info]

count = 0
for i in range(1, len(info)):
    if info[i] > info[i-1]:
        count += 1
print("single increase", count)

count = 0
for i in range(3, len(info)):
    if info[i-3] + info[i-2] + info[i-1] < info[i-2] + info[i-1] + info[i]:
        count += 1
print("sliding window:", count)
