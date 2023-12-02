import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()


def check_bingo(board):
    return (np.isin(np.sum(board, 0), len(board)).any()
            or np.isin(np.sum(board, 1), len(board)).any())


draws = [int(numb) for numb in info[0].split(',')]
boards = []
bingos = []
for i in range(2, len(info), 6):
    boards.append(np.array([[int(num) for num in line.split()] for line in info[i:i+5]]))
    bingos.append(np.zeros(boards[-1].shape))

win_first = []
win_last = []
for draw in draws:
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if draw == boards[i][j][k]:
                    bingos[i][j][k] = 1
        if check_bingo(bingos[i]):
            win_first.append(boards[i].copy())
            win_first.append(bingos[i].copy())
            win_first.append(i)
            win_first.append(draw)
        if np.array([check_bingo(bingos[h]) for h in range(len(bingos))]).all():
            win_last.append(boards[i].copy())
            win_last.append(bingos[i].copy())
            win_last.append(i)
            win_last.append(draw)

def score(result):
    sum = 0
    for i in range(len(result[0])):
        for j in range(len(result[0][0])):
            if result[1][i][j] == 0:
                sum += result[0][i][j]
    return result[2], sum * result[3]


print("win first", score(win_first))
print("win last", score(win_last))