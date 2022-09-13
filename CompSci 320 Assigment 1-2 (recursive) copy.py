
def longest_path():
  
    long_path = []
    for node in range(len(adj_list)):
        for path in recursive_dfs(node, [], {node}):
            if len(path) > len(long_path):
                long_path = path
    return len(long_path) - 1


def recursive_dfs(node, path, seen):
    path = path + [node]
    yield path
    for next_node in adj_list[node]:
        if next_node not in seen:
            yield from recursive_dfs(next_node, path, seen.union(set(adj_list[node])))

#while len(node_stack) > 0:
    #current_node = node_stack.pop()

    #if current_node not in path:
     #   path.append(node)

   # if next_node_index < len(adj_list[next_node_index]):
    #    next_node = int(adj_list[next_node_index])

#return max_length

nodes = 1
max_lengths = []
while nodes != 0:
    nodes = int(input())

    if nodes == 0:
        continue

    global adj_list
    adj_list = []

    for x in range(nodes):
        adj_row = []
        for y in input().split():
            adj_row.append(int(y))
        adj_list.append(adj_row)

    visited = []
    max_length = 0

    #for x in range(nodes):
        #max_length = max(max_length, iterative_dfs(adj_list, x))


    max_lengths.append(longest_path())

for l in max_lengths:
    print(l)

