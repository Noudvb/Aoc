with open("Input.txt") as f:
    info = f.read().splitlines()


def evaluate_expression(numbers, target, current_value=0, concat=False):
    if not numbers:
        return current_value == target
    elif current_value > target:
        return False

    next_number = numbers[0]
    remaining_numbers = numbers[1:]
    if evaluate_expression(remaining_numbers, target, current_value + next_number, concat=concat):
        return True
    elif evaluate_expression(remaining_numbers, target, current_value * next_number, concat=concat):
        return True
    elif concat and evaluate_expression(remaining_numbers, target, int(str(current_value) + str(next_number)), concat=concat):
        return True
    return False


equations = [[int(char) for char in line.replace(":", "").split()] for line in info]

sum1 = 0
sum2 = 0
for equation in equations:
    value = equation[0]
    terms = equation[1:]
    if evaluate_expression(terms, value):
        sum1 += value
    if evaluate_expression(terms, value, concat=True):
        sum2 += value

print("Part1: ", sum1)
print("Part2: ", sum2)

