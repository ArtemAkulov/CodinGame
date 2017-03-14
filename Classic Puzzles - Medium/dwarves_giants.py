###############################################
#                                             #
#     CodinGame Classic Puzzles - Medium      #
# Dwarves Standing on the Shoulders of Giants #
#                                             #
###############################################

def dfs_flood(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
def dfs(tree, entry, dest):
    steps = [(entry, [entry])]
    while steps:
        (leaf, path) = steps.pop()
        for next in tree[leaf] - set(path):
            if next == dest: yield path + [next]
            else: steps.append((next, path + [next]))
def path_valid(path, valid_pairs, direction):
    for i in range(len(path) - 1):
        if direction == 1: pair = [path[i], path[i + 1]]
        else: pair = [path[i + 1], path[i]]
        if not pair in valid_pairs: return False
    return True
n = int(input())
tree = {}
dwarf_heads = []
dwarf_butts = []
valid_pairs = []
for i in range(n):
    xi, yi = [int(j) for j in input().split()]
    dwarf_heads.append(xi)
    dwarf_butts.append(yi)
    valid_pairs.append([xi,yi])
for i in range(len(dwarf_heads)):
    if not dwarf_heads[i] in tree: tree[dwarf_heads[i]] = [dwarf_butts[i]]
    if not dwarf_butts[i] in tree: tree[dwarf_butts[i]] = [dwarf_heads[i]]
    if not dwarf_heads[i] in tree[dwarf_butts[i]]: tree[dwarf_butts[i]].append(dwarf_heads[i])
    if not dwarf_butts[i] in tree[dwarf_heads[i]]: tree[dwarf_heads[i]].append(dwarf_butts[i])    
for i in tree:
    tree[i] = set(tree[i])
sub_trees = []
for i in list(set(dwarf_butts+dwarf_heads)):
    sub_trees.append(list(dfs_flood(tree, i)))
sub_trees = list(map(list, list(set(map(tuple, sub_trees)))))
gargantuan_dwarf = []
teeny_weeny_dwarf = []
for j in range(len(sub_trees)):
    for i in dwarf_heads:
        if not i in dwarf_butts: gargantuan_dwarf.append(i)
    for i in dwarf_butts:
        if not i in dwarf_heads: teeny_weeny_dwarf.append(i)
    
gargantuan_dwarf = list(set(gargantuan_dwarf))
teeny_weeny_dwarf = list(set(teeny_weeny_dwarf))
path_attempt = []
for j in gargantuan_dwarf:
    for i in teeny_weeny_dwarf:
        if len(list(dfs(tree, j, i))) > 0: 
            dwarves_copulating = []
            for k in list(dfs(tree, j, i)): 
                if path_valid(k, valid_pairs, 1): dwarves_copulating.append(k)            
            path_attempt.append(dwarves_copulating)
lengths = []
path_2nd_attempt = []
for m in sum(path_attempt, []):
    lengths.append(len(m))
if lengths.count(len(max(sum(path_attempt, []), key = len))) > 1:
    print(len(max(sum(path_attempt, []), key = len)))
else:
    for k in range(len(path_attempt)):
        path_2nd_attempt.append(list(set(sum(path_attempt[k], []))))
    print(len(max(path_2nd_attempt, key = len)))