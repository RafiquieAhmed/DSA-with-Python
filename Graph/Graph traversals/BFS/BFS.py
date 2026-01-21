        
from collections import deque


class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for x in range(vertex)]
        self.size=vertex
    def addedge(self,src,dest):
        if( 0<= src <self.size and 0 <=dest <self.size):
            #directed graph
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("invaild Edge")
            
          
    def printgraph(self):
        for row in self.mat:
            print(' '.join(map(str,row)))
    
    def BFS(self,src):
        visited =[False] * self.size
        queue =deque([src])
        visited[src]=True
        
        while(queue):
            v=queue.popleft()
            print(v,end=" ")
            for i in range(self.size):
                if(self.mat[v][i]==1 and visited[i]== False):
                    visited[i]=True
                    queue.append(i)
                    
                    
        
g = Graph(8)
g.addedge(0, 1)
g.addedge(0 ,3)
g.addedge(1, 3)
g.addedge(3, 5)
g.addedge(3, 4)
g.addedge(4, 5)
g.addedge(4, 6)
g.addedge(6, 2)
g.addedge(6, 7)

g.BFS(0)
