with open("Input.txt") as f:
    info = f.read().split()

rules = {}
updates = []
for line in info:
    if line.find("|") > 0:
        n1, n2 = map(int, line.split("|"))
        if rules.get(n1) != None:
            rules[n1].append(n2)
        else:
            rules[n1] = [n2]
        if rules.get(n2) == None:
            rules[n2] = []
    else:
        updates.append([int(char) for char in line.split(",")])

def check(l, rules):
    for n in l:
        after = rules.get(n, [])
        for past in after:
            if past in l and l.index(past) < l.index(n):
                return False
    return True


def count_score(lijst):
    sum = 0
    for l in lijst:
        if l:
            sum += l[len(l)//2]
    return sum


def fix_order(j, rules):
    relevant_rules = filter_relevant_rules(rules, j)
    graph = {item: [] for item in j}
    in_degree = {item: 0 for item in j}

    for key, values in relevant_rules.items():
        for value in values:
            graph[key].append(value)
            in_degree[value] += 1

    queue = [node for node in j if in_degree[node] == 0]
    sorted_order = []

    while queue:
        current = queue.pop(0)
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(j):
        raise ValueError("Cycle detected in the rules for the given list.")

    return sorted_order


correct = []
wrong = []
for update in updates:
    if check(update, rules):
        correct.append(update)
    if not check(update, rules):
        wrong.append(update)

print("Part 1:", count_score(correct))


def filter_relevant_rules(rules, item_list):
    filtered_rules = {}
    for key, values in rules.items():
        filtered_values = [value for value in values if value in item_list]
        if key in item_list and filtered_values:
            filtered_rules[key] = filtered_values

    return filtered_rules

fixed_order = []
for ord in wrong:
    fixed_order.append(fix_order(ord, rules))

print("Part 2:", count_score(fixed_order))
