class Graph:
    def __init__(self):
        self.adjlist = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []   

    def addedge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)   # undirected graph

    def displaygraph(self):
        for vertex in self.adjlist:
            print(vertex, "->", self.adjlist[vertex],end='\n')


g = Graph()
g.addedge(1, 2)
g.addedge(2, 3)
g.addedge(1, 4)
g.addedge(4, 3)
g.addedge(2, 4)
g.addedge(4, 5)
g.addedge(3, 5)

g.displaygraph()
