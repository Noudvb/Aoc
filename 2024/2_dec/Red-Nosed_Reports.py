with open("Input.txt") as f:
    info = f.read().splitlines()

def cal_score(arr, part2 = False):
    score = 0
    for line in info:
        arr = [int(i) for i in line.split()]
        if ((all(i < j for i, j in zip(arr, arr[1:])) or
            all(i > j for i, j in zip(arr, arr[1:]))) and
                all(4 > abs(i - j) > 0 for i, j in zip(arr, arr[1:]))):
            score += 1
        elif(part2 == True):
            for i in range(len(arr)):
                new_arr = arr.copy()
                new_arr.pop(i)
                if ((all(i < j for i, j in zip(new_arr, new_arr[1:])) or
                     all(i > j for i, j in zip(new_arr, new_arr[1:]))) and
                        all(4 > abs(i - j) > 0 for i, j in zip(new_arr, new_arr[1:]))):
                    score += 1
                    break
    return score

print("Part 1: ", cal_score(info))

print("Part 2: ", cal_score(info, True))