######################################
#                                    #
# CodinGame Classic Puzzles - Medium #
#          Skynet Revolution         #
#                                    #
######################################

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
                
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

nodes_dict = {}
nodes = []
gateways = []
removed_nodes = []
n, l, e = [int(i) for i in input().split()]

for i in range(n):
    nodes.append([])

for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    nodes[n1].append(str(n2))
    nodes[n2].append(str(n1))
    
for i in range(e):
    ei = int(input())  
    gateways.append(str(ei))

for i in range(n):
    nodes_dict[str(i)] = set(nodes[i])

while True:
    si = int(input()) 

    danger = []
    
    for i in range(len(gateways)):
        danger.append(shortest_path(nodes_dict, str(si), gateways[i]))
        
    if len(min(danger, key=len)) > 2:
        node_to_cut_1 = min(danger, key=len)[0]
        node_to_cut_2 = min(danger, key=len)[1]
    else:    
        node_to_cut_1 = min(danger, key=len)[-2]
        node_to_cut_2 = min(danger, key=len)[-1]

    node_1_index = int(node_to_cut_1)
    node_2_index = int(node_to_cut_2)
    for i in range(len(removed_nodes)):
        if node_1_index > int(removed_nodes[i]):
            node_1_index -= 1
        if node_2_index > int(removed_nodes[i]):
            node_2_index -= 1    


    nodes[node_1_index].remove(node_to_cut_2)
    nodes[node_2_index].remove(node_to_cut_1)

    if nodes[node_1_index] == []:
        nodes.remove(nodes[node_1_index])
        removed_nodes.append(node_to_cut_1)
        if node_to_cut_1 in gateways:
            gateways.remove(node_to_cut_1)

    if nodes[node_2_index] == []:
        nodes.remove(nodes[node_2_index])
        removed_nodes.append(node_to_cut_2)
        if node_to_cut_2 in gateways:        
            gateways.remove(node_to_cut_2)
  
    for i in range(len(nodes)):
        k = 0
        for j in range(len(removed_nodes)):
            if i >= int(removed_nodes[j]):
                k += 1
        nodes_dict[str(i + k)] = set(nodes[i])
        

    print(node_to_cut_1 + ' ' + node_to_cut_2)