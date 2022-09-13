from logging.handlers import RotatingFileHandler
from re import L


def bfs(adj_list, root):
    visited = []
    seen = set()
    seen.add(root)
    visited.append(root)

    while visited:
        if len(seen) == len(adj_list):
            return True
        current = visited.pop(0)
        for node in adj_list[current]:
            if node not in seen:
                seen.add(node)
                visited.append(node)


    return False
    


    



nodes = 1
arborescences = []
while nodes != 0:
    nodes = int(input())
    
    if nodes == 0:
        continue
    
    adj_list = []
    
    for x in range(nodes):
        adj_list.append([int(x) for x in input().split()])

    count = 0
    for y in range(nodes):
        if bfs(adj_list, y) == True:
            count += 1


    arborescences.append(count)


for num in arborescences:
    print(num)

