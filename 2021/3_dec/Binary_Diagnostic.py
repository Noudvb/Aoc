import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

lst = [[int(point) for point in line] for line in info]

gam = ""
eps = ""
for i in range(len(lst[0])):
    tot = 0
    for j in range(len(lst)):
        tot += lst[j][i]
    if tot > len(lst)/2:
        gam += "1"
        eps += "0"
    else:
        gam += "0"
        eps += "1"

print("gamma, epsilon and sum", gam, eps, int(gam, 2)*int(eps, 2))


def rating(arr, majority):
    for i in range(len(arr[0])):
        temp_lst = []

        if len(arr) == 1:
            break
        elif majority is True:
            prime = 0
            if np.sum(arr, 0)[i] >= len(arr) / 2:
                prime = 1
            for k in range(len(arr)):
                if arr[k][i] == prime:
                    temp_lst.append(arr[k])
        else:
            key = 1
            if np.sum(arr, 0)[i]*2 >= len(arr):
                key = 0
            for k in range(len(arr)):
                if arr[k][i] == key:
                    temp_lst.append(arr[k])
        arr = temp_lst
    return arr[0]


print(rating(lst, True))
print(rating(lst, False))

oxygen = "".join([str(char) for char in rating(lst, True)])
CO2 = "".join([str(char) for char in rating(lst, False)])

print("life support rating", int(oxygen, 2)*int(CO2, 2))