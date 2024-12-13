from sympy import symbols, Eq, solve
import re

def solve_equation(A, B, solution, addition=0):
    a, b = symbols('a b')

    eq1 = Eq(int(A[0]) * a + int(B[0]) * b, int(solution[0]) + addition)
    eq2 = Eq(int(A[1]) * a + int(B[1]) * b, int(solution[1]) + addition)

    sol = solve((eq1, eq2), (a, b))

    if sol and all(val.is_integer for val in sol.values()):
        return [int(val) for key, val in sol.items()]
    else:
        return "No solution"

with open("Input.txt") as f:
    info = f.read().splitlines()

puzzle = []
for line in info:
    puzzle.append(re.findall('\d+', line))

cost1 = 0
cost2 = 0
for i in range(0, len(puzzle), 4):
    outcome1 = solve_equation(puzzle[i], puzzle[i+1], puzzle[i+2])
    outcome2 = solve_equation(puzzle[i], puzzle[i + 1], puzzle[i + 2], 10000000000000)
    if not isinstance(outcome1, str):
        cost1 += outcome1[0]*3
        cost1 += outcome1[1]*1
    if not isinstance(outcome2, str):
        cost2 += outcome2[0]*3
        cost2 += outcome2[1]*1

print("Part 1:", cost1)
print("Part 2:", cost2)
