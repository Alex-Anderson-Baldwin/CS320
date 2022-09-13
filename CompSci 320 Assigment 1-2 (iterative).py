def iterative_dfs(adj_list, start):
    node_stack = [start]
    index_stack = [0]
    visited = []
    visiteds = []
    path = []
    if adj_list[start] == ['']:
        return 0

    
    max_length = 0

    while len(node_stack) > 0:

        index = index_stack.pop()
        current_node = node_stack.pop()

        path = path[:index]
        visiteds = visiteds[:index]
        print(index)
        print(visited)
        print(visiteds)
        if len(visiteds) > 0:
            visited = visiteds[-1]



        if current_node not in visited:
            visited.append(current_node)
            path.append(current_node)

        max_length = max(len(path)-1, max_length)

        for node in adj_list[current_node]:
            if int(node) not in node_stack and int(node) not in visited:
                node_stack.append(int(node))
                index_stack.append(len(path))
                
        print(path)
        visiteds.append(visited)


    return max_length

nodes = 1
max_lengths = []

while nodes != 0:
    nodes = int(input())
    
    if nodes == 0:
        continue
    
    adj_list = []
    
    for x in range(nodes):
        adj_list.append(input().split(" "))
    
    visited = []
    max_length = 0

    for x in range(nodes):
        max_length = max(max_length, iterative_dfs(adj_list, x))
    
    max_lengths.append(max_length)

for l in max_lengths:
    print(l)
