import random

#Generates adjacency list of V size for testing various graph theory algorithms
V = 10
def gen_ran(V):
    line = []
    for z in range(V):
        if random.randint(0,1) == 0:
            line.append(0)
        else:
            line.append(random.randint(0,V))
    return line


graph = []
for z in range(V):
    graph.append(gen_ran(V))

for x in range((V)):
    for y in range((V)):
        if y == x:
            graph[x][y] = 0
        if x > y:
            graph[x][y] = graph[y][x]


print(graph)
