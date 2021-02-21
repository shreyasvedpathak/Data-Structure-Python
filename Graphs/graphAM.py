import numpy as np
import sys

sys.path.append('.')
from Queue.queue import Queue
from Stack.stack import Stack


class Graph:
    def __init__(self, vertices, graph_type='directed', weighted = False):
        self._vertices = vertices
        self._type = graph_type
        self._weighted = weighted
        self._adjMAT = np.zeros(shape=(vertices, vertices), dtype=np.int8)

        self._visited = [False] * self._vertices

    def insert_edge(self, u, v, weight=1):
        self._adjMAT[u][v] = weight
        if self._type == 'undirected':
            self._adjMAT[v][u] = weight

    def remove_edge(self, u, v):
        self._adjMAT[u][v] = 0
        if self._type == 'undirected':
            self._adjMAT[v][u] = 0

    def exist_edge(self, u, v):
        return self._adjMAT[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMAT[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMAT[i][j] != 0 and self._weighted == True:
                    print(f'{i} -- {j} = {self._adjMAT[i][j]}')
                elif self._adjMAT[i][j] != 0:
                    print(f'{i} -- {j}')

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMAT[v][j] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMAT[i][v] != 0:
                count += 1
        return count

    def BFS(self, start_vertext):
        i = start_vertext
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
        if self._visited[start_vertex] == False:
            print(start_vertex, end=' ')
            self._visited[start_vertex] = True

            for j in range(self._vertices):
                if self._adjMAT[start_vertex][j] > 0 and self._visited[j] == False:
                    self.DFS_recursive(j)

    def display(self):
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

g.display()
g.edges()
print("DFS Iterative:")
g.DFS_iterative(0)
print("\nDFS Iterative:")
g.DFS_recursive(0)
