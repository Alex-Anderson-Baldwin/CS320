from heapq import heappush, heappop
nodes = 1
costs = []
visited = []
while nodes != 0:
    nodes = int(input())
    if nodes == 0:
        break
    edges = []
    msp = []
    disc = []
    cost = 0
    for x in range(nodes):
        visited.add({x})
        z = x
        for y in input().split(", ")[x+1:]:
            z+=1 
            if int(y) != 0:
                heappush(edges, (int(y), x, z)) 
    count = 0 
    while len(msp) < nodes-1:
        temp = heappop(edges)
        print(count)
        if (temp[1],temp[2]) not in msp:
                visited[]
                cost+= temp[0]
                msp.append((temp[1], temp[2]))
                

    costs.append(cost)
for cost in costs:
    print(cost)

