from functools import lru_cache


def possible_design(available_patterns, design):
    @lru_cache
    def helper(design):
        if not design:
            return True
        for pattern in available_patterns:
            if design.startswith(pattern):
                if helper(design[len(pattern):]):
                    return True
        return False
    return helper(design)


def arrangement_designs(available_patterns, design):
    @lru_cache
    def helper(design):
        count = 0
        if not design:
            return 1
        for pattern in available_patterns:
            if design.startswith(pattern):
                count += helper(design[len(pattern):])
        return count
    return helper(design)


with open("Input.txt") as f:
    info = f.read().splitlines()


patterns = info[0].split(", ")
designs = info[2:]

possible = 0
arrangement = 0
for i, design in enumerate(designs):
    possible += possible_design(patterns, design)
    arrangement += arrangement_designs(patterns, design)

print("Part 1: ", possible)
print("Part 2: ", arrangement)
