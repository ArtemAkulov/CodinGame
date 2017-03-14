#########################################
#                                       #
#  CodinGame Classic Puzzles - Medium   #
#       Teads Sponsored Contest         #
#                                       #
#########################################

def bfs(tree, entry):
    steps, path = set(), [entry]
    while path:
        leaf = path.pop(0)
        if not leaf in steps:
            steps.add(leaf)
            path.extend(tree[leaf] - steps)
    return leaf
def dfs(tree, entry, dest):
    steps = [(entry, [entry])]
    while steps:
        (leaf, path) = steps.pop()
        for next in tree[leaf] - set(path):
            if next == dest: yield path + [next]
            else: steps.append((next, path + [next]))
n = int(input())
tree = {}
for i in range(n):
    xi, yi = [int(j) for j in input().split()]
    if not xi in tree: tree[xi] = [yi]
    if not yi in tree: tree[yi] = [xi]
    if not xi in tree[yi]: tree[yi].append(xi)
    if not yi in tree[xi]: tree[xi].append(yi)    
for i in tree:
    tree[i] = set(tree[i])       
dark_side = bfs(tree, xi)
bright_side = bfs(tree, dark_side)
longest_path = list(dfs(tree, dark_side, bright_side))[0]
print(len(longest_path)//2)