from heapq import heappush, heappop
nodes = 1
costs = []


while nodes != 0:
    visited = set()
    nodes = int(input())
    if nodes == 0:
        break
    msp = []
    adj_list = []
    total = 0
    for x in range(nodes):
        z = 0
        adj_list.append([])
        for y in input().split(" "): 
            if int(y) != 0:
                adj_list[x].append((int(y), z))
            z+=1
    edges = [(0,0)]
    while len(edges) > 0:
        cost, currentNode = heappop(edges)
        if currentNode not in visited:
            visited.add(currentNode)
            total += cost
            for a,b in adj_list[currentNode]:
                if b not in visited:
                    heappush(edges, (a,b))

    costs.append(total)
for c in costs:
    print(c)
