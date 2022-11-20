import numpy as np
from dsa06_QueueADT.queue_linked import QueueLinked


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
        self._visited = [0] * vertices

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j]:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j]:
                    print(i, '--', j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j]:
                count += 1

        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v]:
                count += 1
        return count

    def display_adjMat(self):
        print(self._adjMat)

    def search_BFS(self, s):
        i = s
        q = QueueLinked()
        visited = [0] * self._vertices
        print(i, end=' ')
        visited[i] = 1
        q.enqueue(i)

        while not q.is_empty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1
                    q.enqueue(j)

    def search_DFS(self, s):
        if self._visited[s] == 0:
            print(s, end=' ')
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._visited[j] == 0:
                    self.search_DFS(j)


# Undirected Graph
def undirected():
    G = Graph(4)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.insert_edge(0, 1)
    G.insert_edge(0, 2)
    G.insert_edge(1, 0)
    G.insert_edge(1, 2)
    G.insert_edge(2, 0)
    G.insert_edge(2, 1)
    G.insert_edge(2, 3)
    G.insert_edge(3, 2)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.edges()
    print('Edge Between 1-3', G.exist_edge(1, 3))
    print('Edge Between 1-2', G.exist_edge(1, 2))
    print('Degree', G.indegree(2))
    G.remove_edge(1, 2)
    print('Degree', G.indegree(2))
    print('Edge Between 1-2', G.exist_edge(1, 2))
    G.search_DFS(0)


# Weighted Undirected  Graph
def weighted_undirected():
    G = Graph(4)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.insert_edge(0, 1, 26)
    G.insert_edge(0, 2, 16)
    G.insert_edge(1, 0, 26)
    G.insert_edge(1, 2, 12)
    G.insert_edge(2, 0, 16)
    G.insert_edge(2, 1, 12)
    G.insert_edge(2, 3, 8)
    G.insert_edge(3, 2, 8)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.edges()
    print('Edge Between 1-3', G.exist_edge(1, 3))
    print('Edge Between 1-2', G.exist_edge(1, 2))
    print('Degree', G.indegree(2))
    G.remove_edge(1, 2)
    print('Degree', G.indegree(2))
    print('Edge Between 1-2', G.exist_edge(1, 2))


def directed():
    G = Graph(4)
    G.display_adjMat()
    print("Vertices:", G.vertex_count())
    G.insert_edge(0, 1)
    G.insert_edge(0, 2)
    G.insert_edge(1, 2)
    G.insert_edge(2, 3)
    G.display_adjMat()
    G.edges()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.edges()
    print('Edge Between 1-3', G.exist_edge(1, 3))
    print('Edge Between 1-2', G.exist_edge(1, 2))
    print('Degree', G.indegree(2))
    G.remove_edge(1, 2)
    print('Degree', G.indegree(2))
    print('Edge Between 1-2', G.exist_edge(1, 2))


def weighted_directed():
    G = Graph(4)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.insert_edge(0, 1, 26)
    G.insert_edge(0, 2, 16)
    G.insert_edge(1, 2, 12)
    G.insert_edge(2, 3, 8)
    G.display_adjMat()
    print('Vertices:', G.vertex_count())
    print('Edges:', G.edge_count())
    G.edges()
    print('Edge Between 1-3', G.exist_edge(1, 3))
    print('Edge Between 1-2', G.exist_edge(1, 2))
    print('Degree', G.indegree(2))
    G.remove_edge(1, 2)
    print('Degree', G.indegree(2))
    print('Edge Between 1-2', G.exist_edge(1, 2))


if __name__ == "__main__":
    undirected()
