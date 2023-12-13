from functools import cache

with open('input.txt') as f:
    lines = f.read().splitlines()

@cache
def find_arrangements(line, arrangement):
    if line.count('#') == 0 and len(arrangement) == 0:
        return 1
    elif len(line) == 0 or len(arrangement) == 0 or len(line) < arrangement[0] or (len(arrangement) == 0 and line.count('#') > 0):
        return 0

    if line[0] == '.':
        return find_arrangements(line[1:], arrangement)

    elif line[0] == '#' and all(char != '.' for char in line[:arrangement[0]]) and (len(line) == arrangement[0] or line[arrangement[0]] != '#'):
        return find_arrangements(line[arrangement[0]+1:], arrangement[1:])

    elif line[0] == '?':
        if all(char != '.' for char in line[:arrangement[0]]) and (len(line) == arrangement[0] or line[arrangement[0]] != '#'):
            return find_arrangements(line[arrangement[0]+1:], arrangement[1:]) + find_arrangements(line[1:], arrangement)
        return find_arrangements(line[1:], arrangement)
    return 0


lines = [[string, list(map(int, groups.split(',')))] for string, groups in [line.split() for line in lines]]


def temp(lines, n):
    sum = 0
    for string, groups in lines:
        sum += find_arrangements(string+('?' + string)*(n-1) + '.', tuple(groups*n))
    return sum

print('answer part 1:', temp(lines, 1))
print('answer part 2:', temp(lines, 5))