with (open("input.txt") as f):
    info = f.read().splitlines()

info = [[point for point in line] for line in info]

start = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

scores_close = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

scores_open = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

cor_value = 0
open = []
for line in info:
    end = []
    for char in line:
        if char in start.keys():
            end.append(start[char])
        elif end[-1] == char:
            end.pop()
        elif char in start.values():
            cor_value += scores_close[char]
            end = []
            break
    if end:
        end.reverse()
        open.append(end)

print(cor_value)

scores = []
for line in open:
    score = 0
    for char in line:
        score *= 5
        score += scores_open[char]
    scores.append(score)
scores.sort()
print(scores[int((len(scores)-1)/2)])

