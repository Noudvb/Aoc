import re

with open("Input.txt") as f:
    info = f.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"

sum1 = 0
sum2 = 0
result = re.finditer(pattern, info)

do = True
for match in result:
    if match.group() != "don't()" and match.group() != "do()":
        sum1 += int(match.group(1)) * int(match.group(2))
        if do:
            sum2 += int(match.group(1)) * int(match.group(2))
    elif match.group() == "don't()":
        do = False
    elif match.group() == "do()":
        do = True

print("part 1: ", sum1)
print("part 2: ", sum2)