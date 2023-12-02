import numpy as np

with open("input.txt") as f:
    info = f.read().splitlines()

connections = {}
for path in info:
    begin, end = path.split("-")
    if begin not in connections.keys():
        connections[begin] = []
    if end not in connections.keys():
        connections[end] = []
    connections[begin].append(end)
    connections[end].append(begin)


def path_finder(path, next, twice=True):
    if next == 'end':
        return 1
    elif next not in path:
        new_path = path.copy()
        new_path.append(next)
        return sum(path_finder(new_path, go, twice) for go in connections[next])
    elif next in path and next.isupper():
        new_path = path.copy()
        new_path.append(next)
        return sum(path_finder(new_path, go, twice) for go in connections[next])
    elif next in path and next.islower() and twice and next != 'start':
        new_path = path.copy()
        new_path.append(next)
        twice = False
        return sum(path_finder(new_path, go, twice) for go in connections[next])
    return 0

print(path_finder([], 'start', False))
print(path_finder([], 'start'))
