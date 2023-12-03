with open("input.txt") as f:
    info = f.read().splitlines()

poly_temp = info[0]
insert = {}
pair_score = {}
score = {}
for action in info[2:]:
    pair, key = action.split(" -> ")
    insert[pair] = [pair[0]+key, key+pair[1]]
    pair_score[pair] = 0
    score[key] = 0

score[poly_temp[0]] += 1
score[poly_temp[-1]] += 1
empty_pair_score = pair_score.copy()

for i in range(1, len(poly_temp)):
        pair_score[poly_temp[i-1:i+1]] += 1

for i in range(40):
    for pair in pair_score:
        for add_pair in insert[pair]:
            empty_pair_score[add_pair] += pair_score[pair]
    pair_score = empty_pair_score.copy()
    for entry in empty_pair_score:
        empty_pair_score[entry] = 0


for set in pair_score:
    for let in set:
        score[let] += pair_score[set]

scores = []
for letter in score:
    scores.append(score[letter]/2)

print(max(scores)-min(scores))