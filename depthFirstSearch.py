import time
class  Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u,v):
        self.graph.setdefault(u,[]).append(v)

    def dfs(self, start, visited=None):
        visited = visited or set()
        start_time = time.time()

        def dfs_recursive(node):
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.graph.get(node,[]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        print(f"\nTotal time of traversal : {time.time() - start_time:.6f} seconds")

graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(2,5)
graph.add_edge(3,6)
graph.add_edge(3,7)

print("DFS traversal starting from node 1: ")
graph.dfs(1)