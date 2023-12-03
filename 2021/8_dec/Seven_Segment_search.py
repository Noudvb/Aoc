import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

output = [line[line.index("|")+2:] for line in info]
output = [line.split(" ") for line in output]
input = [line[:line.index("|")-1] for line in info]
input = [line.split(" ") for line in input]

count = np.zeros(4)
for numbers in output:
    for num in numbers:
        if len(num) == 2:
            count[0] += 1
        elif len(num) == 4:
            count[1] += 1
        elif len(num) == 3:
            count[2] += 1
        elif len(num) == 7:
            count[3] += 1
print(sum(count))


def subtract(word1, word2):
    for let in word1:
        word2 = word2.replace(let, "")
    return word2


def decode(input):
    result = {}
    input = [''.join(sorted(entry)) for entry in input]
    input.sort(key=len)

    result['1'] = input[0]
    result['7'] = input[1]
    result['4'] = input[2]
    result['8'] = input[9]

    for num in input[3:6]:
        if result['1'][0] in num and result['1'][1] in num:
            result['3'] = num
        elif sum([1 for char in num if char in result['4']]) == 3:
            result['5'] = num
        else:
            result['2'] = num

    for num in input[6:9]:
        if sum([1 for char in num if char in result['3']]) == 5:
            result['9'] = num
        elif result['1'][0] in num and result['1'][1] in num:
            result['0'] = num
        else:
            result['6'] = num
    return {v: k for k, v in result.items()}


score = 0
for i in range(len(input)):
    decript = decode(input[i])
    first_num = [''.join(sorted(entry)) for entry in output[i]].copy()
    result = ''
    for number in first_num:
        result += decript[number]
    score += int(result)

print(score)