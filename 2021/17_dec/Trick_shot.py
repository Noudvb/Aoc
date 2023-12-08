with open("input.txt") as f:
    info = f.read().splitlines()

xmin = 209
xmax = 238
ymin = -86
ymax = -59

def model(xvel, yvel):
    xpos = 0
    ypos = 0
    ypositions = []
    while True:
        xpos += xvel
        ypos += yvel
        ypositions.append(ypos)
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return max(ypositions)
        xvel = max(xvel - 1, 0)
        yvel -= 1
        if ypos < ymin or xpos > xmax:
            return False

def quadraticsolver(a, b, c):
    d = (b ** 2) - (4 * a * c)

    sol1 = (-b - d**0.5) / (2 * a)
    sol2 = (-b + d**0.5) / (2 * a)
    return round(max(sol1, sol2))

minxspeed = quadraticsolver(1, 1, -2*xmin)
maxxspeed = quadraticsolver(1, 1, -2*xmax)

shots = []
for i in range(100):
    result = model(minxspeed, i)
    if result:
        shots.append(result)

print('answer part 1: ', max(shots))

def model2(xvel, yvel):
    xpos = 0
    ypos = 0
    duh = 0
    while duh == 0:
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return True
        xpos += xvel
        ypos += yvel
        xvel -= 1
        xvel = max(xvel, 0)
        yvel -= 1
        if ypos < ymin or xpos > xmax:
            return False

attempts = 0
for i in range(minxspeed, xmax+1):
    for j in range(ymin-1, 200):
        if model2(i, j) is True:
            attempts += 1

print(attempts)
print('answer to part 2: ', attempts)
