with open("input.txt") as f:
    info = f.read().split()

# part 1
#################################
# characters = [[char for char in line if char.isnumeric()] for line in info]
# numbers = [int(line[0]+line[-1]) for line in characters]
#
# print(characters)
# print(numbers)
# print(sum(numbers))

# part 2
####################################
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
sum = 0
for line in info:
    smallest_key = 99999999999
    largest_key = -1
    for i in range(len(line)):
        sub_line = line[i:]
        for number in numbers.keys():
            if number in sub_line and sub_line.find(number)+i < smallest_key:
                smallest_key = sub_line.find(number)+i
                smallest_number = numbers[number]
            if number in sub_line and sub_line.find(number)+i > largest_key:
                largest_key = sub_line.find(number)+i
                largest_number = numbers[number]

    char_arr = [char for char in line]
    for i, char in enumerate(char_arr):
        if char.isnumeric() and i < smallest_key:
            smallest_key = i
            smallest_number = int(char)
        if char.isnumeric() and i > largest_key:
            largest_key = i
            largest_number = int(char)

    sum += int(str(smallest_number)+str(largest_number))

print(sum)

# 53779 to high
# 53259 to low
