import numpy as np
import sys

sys.path.append('.')
from Queue.queue import Queue
from Stack.stack import Stack


class Graph:
    def __init__(self, vertices, graph_type='directed', weighted = False):
        '''
        Initialises Adjacent Matrix with Zeros and other class variables.

        Parameters:
        vertices -- number of vertices
        graph_type -- 'directed' or 'undirected'
        weighted -- True or False
        '''
        self._vertices = vertices
        self._type = graph_type
        self._weighted = weighted
        self._adjMAT = np.zeros(shape=(vertices, vertices), dtype=np.int8)

        self._visited = [False] * self._vertices

    def insert_edge(self, u, v, weight=1):
        '''
        Adds an edge between the passed vertices (u,v) by allocating the weight at that index position.
        If the graph is 'undirected', then same weights are also copied to (v,u).
        '''
        self._adjMAT[u][v] = weight
        if self._type == 'undirected':
            self._adjMAT[v][u] = weight

    def remove_edge(self, u, v):
        '''
        Removes an edge between the passed vertices (u,v) by making that index position as 0.
        If the graph is 'undirected', then 0 is also copied to (v,u).
        '''
        self._adjMAT[u][v] = 0
        if self._type == 'undirected':
            self._adjMAT[v][u] = 0

    def exist_edge(self, u, v):
        '''
        Returns True if edge exists between vertices (u,v), else False.
        '''
        return self._adjMAT[u][v] != 0

    def vertex_count(self):
        '''
        Returns number of vertices present in the Graph.
        '''
        return self._vertices

    def edge_count(self):
        '''
        Returns number of edges present in the Graph.
        '''
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMAT[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        '''
        Prints all the vertices.
        '''
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        '''
        Prints all the edges with weights if the graph is undirected.
        '''
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMAT[i][j] != 0 and self._weighted == True:
                    print(f'{i} -- {j} = {self._adjMAT[i][j]}')
                elif self._adjMAT[i][j] != 0:
                    print(f'{i} -- {j}')

    def outdegree(self, v):
        '''
        Returns the outdegree of the passed vertex v.
        '''
        count = 0
        for j in range(self._vertices):
            if self._adjMAT[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        '''
        Returns the indegree of the passed vertex v.
        '''
        count = 0
        for i in range(self._vertices):
            if self._adjMAT[i][v] != 0:
                count += 1
        return count

    def BFS(self, start_vertex):
        '''
        Breadth First Search
        '''
        i = start_vertex
        q = Queue()
        visited = [False] * self._vertices
        print(i, end=' ')
        visited[i] = True
        q.enqueue(i)

        while not q.isempty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMAT[i][j] > 0 and visited[j] == False:
                    print(j, end=' ')
                    visited[j] = True
                    q.enqueue(j)

    def DFS_iterative(self, start_vertex):
        '''
        Depth First Search using Stack.
        '''
        i = start_vertex
        s = Stack()
        visited = [False] * self._vertices
        s.push(i)
        while not s.isempty():
            i = s.pop()
            if (not visited[i]):
                print(i, end=' ')
                visited[i] = True
            for j in range(self._vertices):
                if self._adjMAT[i][j] > 0:
                    if (not visited[j]):
                        s.push(j)

    def DFS_recursive(self, start_vertex):
        '''
        Depth First Search using Recursion.
        '''
        if self._visited[start_vertex] == False:
            print(start_vertex, end=' ')
            self._visited[start_vertex] = True

            for j in range(self._vertices):
                if self._adjMAT[start_vertex][j] > 0 and self._visited[j] == False:
                    self.DFS_recursive(j)

    def display(self):
        '''
        Displays Adjacency Matrix.
        '''
        n_edges = self.edge_count()
        if self._type == 'undirected':
            n_edges = int(n_edges / 2)

        print(self._adjMAT)
        print("Vertices: ", self.vertex_count())
        print("Edges: ", n_edges)


g = Graph(7, graph_type='directed', weighted = True)

g.insert_edge(0, 1, 20)
g.insert_edge(0, 5, 20)
g.insert_edge(0, 6, 20)

g.insert_edge(1, 0, 40)
g.insert_edge(1, 2, 40)
g.insert_edge(1, 5, 40)
g.insert_edge(1, 6, 40)

g.insert_edge(2, 3, 30)
g.insert_edge(2, 4, 30)
g.insert_edge(2, 6, 30)

g.insert_edge(3, 4, 10)

g.insert_edge(4, 2, 50)
g.insert_edge(4, 5, 50)

g.insert_edge(5, 2, 60)
g.insert_edge(5, 3, 60)

g.insert_edge(6, 3, 70)

print("\nAdjacency Matrix")
g.display()

print("\nEdges")
g.edges()

print("\nBFS:")
g.BFS(0)

print("\nDFS Iterative:")
g.DFS_iterative(0)

print("\nDFS Iterative:")
g.DFS_recursive(0)
