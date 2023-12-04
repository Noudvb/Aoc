import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

cards = [[[int(num) for num in sec.split()] for sec in card[card.index(": ")+2:].split(" | ")] for card in info]
print('score for part 1:', sum([2 ** (len(set(card[0]).intersection(set(card[1]))) - 1) for card in cards if len(set(card[0]).intersection(set(card[1]))) > 0]))

scores = [len(set(card[0]).intersection(set(card[1]))) for card in cards]

total = np.ones(len(scores))
for i, score in enumerate(scores):
    begin = min(i+1, len(scores))
    end = min(i+score+1, len(scores))
    total[begin:end] += np.ones(end-begin) * total[i]
print('score for part 2:', int(sum(total)))