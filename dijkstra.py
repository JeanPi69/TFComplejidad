import sys 
import time

class Graph(): 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
   
    def printSolution(self, dist): 
        print ("Distancias desde origen") 
        for node in range(self.V): 
            print (node, "-", dist[node]) 
   
    def minDistance(self, dist, shortPathSet):         """ n """
   
        min = sys.maxsize 
   
        for v in range(self.V):                         """ n """
            if dist[v] < min and shortPathSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index

    def dijkstra(self, initPoint):                      """ n^2 """
   
        dist = [sys.maxsize] * self.V                   """ 1 """
        dist[initPoint] = 0                             """ 1 """
        shortPathSet = [False] * self.V                 """ 1 """
   
        for _ in range(self.V):                         """ n """

            u = self.minDistance(dist, shortPathSet)    """ n """
            shortPathSet[u] = True
   
            for v in range(self.V):                     """ n """
                if self.graph[u][v] > 0 and shortPathSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: """ 1 """
                    dist[v] = dist[u] + self.graph[u][v]                                                       """ 1 """
    
        self.printSolution(dist)                                                                               """ 1 """




start_time = time.time()   
g = Graph(9) 
g.graph = [[0, 4, 0, 3, 0, 0, 4, 8, 0], 
           [4, 0, 8, 0, 5, 0, 2, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 1, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 2, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 4, 0, 1, 0, 7], 
           [7, 0, 2, 0, 0, 0, 6, 7, 0]]; 

g.dijkstra(0)
print("Tiempo de ejecución:  %s segundos" % (time.time() - start_time))