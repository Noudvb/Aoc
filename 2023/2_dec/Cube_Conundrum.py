with open("input.txt") as f:
    info = f.read().splitlines()

total = 0
for line in info:
    result = line.split(":")
    game = int(result[0].split(" ")[1])
    draw = result[1].split(";")
    total += game
    for colors in draw:
        failed = False
        for color in colors.split(","):
            color_res = color.split(" ")
            col = color_res[2]
            num = int(color_res[1])
            if col == "red" and num > 12:
                total -= game
                failed = True
                break
            if col == "green" and num > 13:
                total -= game
                failed = True
                break
            if col == "blue" and num > 14:
                total -= game
                failed = True
                break
        if failed:
            break
total = 0
for line in info:
    result = line.split(":")
    game = int(result[0].split(" ")[1])
    draw = result[1].split(";")
    total += game
    for colors in draw:
        failed = False
        for color in colors.split(","):
            color_res = color.split(" ")
            col = color_res[2]
            num = int(color_res[1])
            if col == "red" and num > 12:
                total -= game
                failed = True
                break
            if col == "green" and num > 13:
                total -= game
                failed = True
                break
            if col == "blue" and num > 14:
                total -= game
                failed = True
                break
        if failed:
            break
print(total, "part 1")


#### part 2
powers = 0
for line in info:
    result = line.split(":")
    game = int(result[0].split(" ")[1])
    draw = result[1].split(";")
    power = 0
    min_red = 0
    min_green = 0
    min_blue = 0
    for colors in draw:
        for color in colors.split(","):
            color_res = color.split(" ")
            col = color_res[2]
            num = int(color_res[1])
            if col == "red":
                min_red = max(min_red, num)
            if col == "green":
                min_green = max(min_green, num)
            if col == "blue":
                min_blue = max(min_blue, num)
    powers += min_red*min_green*min_blue
print(powers)
