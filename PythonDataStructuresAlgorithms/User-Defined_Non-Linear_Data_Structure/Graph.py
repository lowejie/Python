# Graph is a collection of vertices and edges
# Vertices represent data and edges represent relationship between vertices

# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # allocate memory for the adjacency list
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest) in edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append(dest)

def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighbouring vertices
        for dest in graph.adjList[src]:
            print(f'({src} -> {dest})', end='')
        print()

if __name__ == '__main__':

    # Input: Edges in a directed graph
    edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 2), (4, 5), (5, 4)]

    # No. of vertices (labelled from 0 to 5)
    n = 6

    # construct a graph from a given list of edges
    graph = Graph(edges, n)

    # print adjacency list representation of the graph
    printGraph(graph)

# Breath-first Search (BFS)

import collections
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("BFS traversal: ")
    bfs(graph, 0)


# Depth-first Search (DFS)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1','2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2','3'])
}

dfs(graph, '0')