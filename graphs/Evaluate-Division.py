class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        # build adjacency list => a: [b, a/b] for eqn in equations
        for i, eqn in enumerate(equations):
            a, b = eqn
            adj[a].append([b, values[i]])
            adj[b].append([a, (1 / values[i])])
        
        def bfs(src, dest):
            # edge cases
            if src not in adj or dest not in adj:
                return -1

            queue, visited = deque(), set()
            # queue consists of src, w pairs, w = product of weights from src to current vertice
            queue.append([src, 1])
            visited.add(src)

            while queue:
                node, w = queue.popleft()
                if node == dest:
                    return w
                else:
                    for neighbor, weight in adj[node]:
                        if neighbor not in visited:
                            queue.append([neighbor, w * weight])
                            visited.add(neighbor)
            return -1   # if no path exists between src and dest

        # go through queries, find path from numerator to denominator using bfs 
        return [bfs(q[0], q[1]) for q in queries]
        