import copy
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  
        self. ROW = len(graph)
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def breadth_first_search(self, s, t, parent):
 

        visited = [False]*(self.ROW)
 

        queue = []
 

        queue.append(s)
        visited[s] = True
 

        while queue:
 

            u = queue.pop(0)
 

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:

                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
 

        return False
             
     
    def find_path(self, source, sink):
 
        parent = [-1]*(self.ROW)
 
        max_flow = 0
 

        while self.breadth_first_search(source, sink, parent) :
 

            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 

            max_flow +=  path_flow
 

            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
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



    graph = [[0 for x in range(len(adj_list)*2)] for y in range(len(adj_list)*2)]
    for x in range(len(adj_list)):
        for y in adj_list[x]:
            graph[2*x+1][2*int(y)] = 1
        graph[2*x][2*x+1] = 1
 

    max_congestion = 0 

    for source in range(1, len(graph), 2):
        for sink in range(source + 1, len(graph), 2):
            if sum(vertex for vertex in graph[sink+1]) > max_congestion:
                sliced_graph = copy.deepcopy(graph)
                g = Graph(sliced_graph)
                max_congestion = max(g.find_path(source, sink), max_congestion)

    max_congestions.append(max_congestion)


for x in max_congestions:
    print(x)
