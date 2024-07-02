from sympy import *
import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

traject = [[[int(item) for item in cor.replace(",", "").split()] for cor in line.split(' @ ')] for line in info]

class Line:
    def __init__(self, ycoeff, xcoeff, const):
        self.a = ycoeff
        self.b = xcoeff
        self.c = const

    def findSolution(L1, L2):
        x = ((L1.a*L2.c)-(L2.a*L1.c))/((L2.a*L1.b)-(L1.a*L2.b))
        y = (L1.b*x+L1.c)/L1.a
        return (x,y)


count = 0
for i, A in enumerate(traject):
    for B in range(i+1, len(traject)):
        # print("A", A)
        # print(B, 'B', traject[B])
        B = traject[B]

        a = np.array([[A[1][0], A[1][1]], [-B[1][0], -B[1][1]]]).T
        b = np.array([B[0][0]-A[0][0], B[0][1]-A[0][1]])
        try:
            x = np.linalg.solve(a, b)
            if 200000000000000 <= A[0][0] + A[1][0]*x[0] <= 400000000000000 and 200000000000000 <= A[0][1] + A[1][1]*x[0] <= 400000000000000 and x[0] >= 0 and x[1] >= 0:
                count += 1
            # print(x)
            # print(A[0][0] + A[1][0]*x[0], A[0][1] + A[1][1]*x[0], '\n')
        except np.linalg.LinAlgError:
            # print('error')
            continue

print(count)
