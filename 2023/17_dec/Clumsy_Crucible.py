import numpy as np
import heapq

with open("input.txt") as f:
    info = f.read().splitlines()

grid = np.array([[int(char) for char in line] for line in info])


def heat_map(root, grid, flowmin, flowmax):
    seen = set()
    pq = [(0, root, root)]
    height, width = np.shape(grid)
    cheapmap = np.full((height, width), np.inf)
    cheapmap[root] = 0
    options = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while pq:
        heat, (x, y), (old_x, old_y) = heapq.heappop(pq)
        if (x, y, old_x, old_y) in seen:
            continue
        seen.add((x, y, old_x, old_y))

        for i, j in options:
            heattemp = heat
            if (i == old_y and j == old_x) or (i == -old_y and j == -old_x):
                continue

            elif 0 <= x + (i * (flowmin - 1)) < height and 0 <= y + (j * (flowmin - 1)) < width:
                for h in range(1, flowmin):
                    x_new, y_new = x + (i * h), y + (j * h)
                    heattemp += grid[x_new][y_new]

            for flow in range(flowmin, flowmax + 1):
                x_new, y_new = x + (i * flow), y + (j * flow)
                if 0 <= x_new < height and 0 <= y_new < width:
                    heattemp += grid[x_new][y_new]
                    if heattemp < cheapmap[x_new][y_new]:
                        cheapmap[x_new][y_new] = heattemp
                    heapq.heappush(pq, (heattemp, (x_new, y_new), (j, i)))
                else:
                    break
    return cheapmap[-1][-1]


print('answer to part 1:', heat_map((0,0), grid, 1, 3))
print('answer to part 2:', heat_map((0,0), grid, 4, 10))
