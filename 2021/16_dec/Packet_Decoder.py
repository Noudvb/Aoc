with open("input.txt") as f:
    info = f.read().splitlines()

bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def strtobin(string):
    str = ''
    for char in string:
        str += bin[char]
    return str


def prod(arr):
    result = 1
    for num in arr:
        result *= num
    return result


def calscore(Id, scores):
    if Id == 0:
        return sum(scores)
    elif Id == 1:
        return prod(scores)
    elif Id == 2:
        return min(scores)
    elif Id == 3:
        return max(scores)
    elif Id == 5 and scores[0] > scores[1]:
        return 1
    elif Id == 6 and scores[0] < scores[1]:
        return 1
    elif Id == 7 and scores[0] == scores[1]:
        return 1
    return 0


def bintoval(string):
    version = int(string[:3], 2)
    ID = int(string[3:6], 2)
    string = string[6:]
    score = 0
    if ID == 4:
        value = ''
        for i in range(0, len(string), 5):
            value += string[i + 1:i + 5]
            if string[i] == '0':
                return int(value, 2), string[i + 5:], version
    elif string[0] == '0':
        L = int(string[1:16], 2)
        temp_string = string[16:16 + L]
        string = string[16 + L:]
        scores = []
        while len(temp_string) >= 11:
            scoretemp, temp_string, version2 = bintoval(temp_string)
            scores.append(scoretemp)
            version += version2
        print('0:')
        print('Id: ', ID)
        print(scores)
        score = calscore(ID, scores)
    elif string[0] == '1':
        N = int(string[1:12], 2)
        string = string[12:]
        scores = []
        for i in range(N):
            scoretemp, string, version3 = bintoval(string)
            scores.append(scoretemp)
            version += version3
        print('1:')
        print('Id: ', ID)
        print(scores)
        score = calscore(ID, scores)
    return score, string, version


bina = strtobin(info[0])
result = bintoval(bina)

print('answer part 1: ', result[2])
print('answer part 2: ', result[0])