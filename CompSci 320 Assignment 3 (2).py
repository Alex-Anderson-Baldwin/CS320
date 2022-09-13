import copy
import time 
class Graph:
  
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(self.graph)
         
    def breadth_first_search(self, s, t, parent):
 
        visited =[False]*(self.ROW)
         
        queue=[]
         
        queue.append(s)
        visited[s] = True
          
        while queue:
 
            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False
             
     
    def get_paths(self, source, sink):
 
        parent = [-1]*(self.ROW)
 
        max_flow = 0 
 
        while self.breadth_first_search(source, sink, parent) :
            #path_flow = float("Inf")
            s = sink
            while(s !=  source):
              #  path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
           # max_flow +=  path_flow
            max_flow +=  1
            v = sink
            while(v !=  source):
                u = parent[v]
                #self.graph[u][v] -= path_flow
                #self.graph[v][u] += path_flow
                self.graph[u][v] -= 1
                self.graph[v][u] += 1
                v = parent[v]
 
        return max_flow
    

 

max_congestions = []
nodes = 1
while nodes != 0:
    nodes = int(input())
    
    if nodes == 0:
        continue
    
    adj_list = []
    
    for x in range(nodes):
        adj_list.append(input().strip().split(" ") ) 



    graph = []
    for node in adj_list:
        row = [0 for x in range(len(adj_list))]
        for edge in node:
            row[int(edge)] = 1
        graph.append(row)

 
 
    """pairs = set() 

    for x in range(len(adj_list)):
        for y in range(len(adj_list)):
            if x != y:
                if x > y:
                    pairs.add((x, y))
                else:
                    pairs.add((y,x))"""

    max_congestion = 0
    for source in range(len(adj_list)):
        for sink in range(source+1, len(adj_list)):
            g = Graph(copy.deepcopy(graph))
            max_congestion = max(g.get_paths(source, sink), max_congestion)

    max_congestions.append(max_congestion)


for x in max_congestions:
    print(x)
