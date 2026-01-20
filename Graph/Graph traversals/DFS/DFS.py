
            

                


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
            

#for testing            
    def printgraph(self):
        for row in self.mat:
            print(' '.join(map(str,row)))
    
    def dfs(self,src):
        visited =[False] * self.size
        stack=[src]
        
        while(stack):
            vertex =stack.pop()
            
            if (visited[vertex] ==False):
                print(vertex, end =" ->")
                visited[vertex] =True
                
            for i in range(self.size):
                if self.mat[vertex][i] ==1 and visited[i] ==False:
                    stack.append(i)
        
g = Graph(6)
g.addedge(0, 1)
g.addedge(0 ,2)
g.addedge(2, 3)
g.addedge(2, 4)
g.addedge(3, 5)
g.addedge(4, 5)

g.dfs(0)
