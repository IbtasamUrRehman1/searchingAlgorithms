from collections import deque
import time


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)


# Assuming the graph is represented as an adjancy list using dictionaries
# Where keys are verteces and vlaues are lists adjcent vertices

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_vertex = 'A'
# Measure the time taken for BFS
start_time = time.time()
bfs(graph, start_vertex)
end_time = time.time()

print("\nTime taken for BFS: {:.6f} seconds".format(end_time - start_time))
