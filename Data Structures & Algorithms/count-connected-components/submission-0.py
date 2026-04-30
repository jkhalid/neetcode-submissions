class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        node_map = {node:[] for node in range(n)}
        visit = [False] * n
        for node, edge in edges:
            node_map[node].append(edge)
            node_map[edge].append(node)

        def dfs(node):
            for vertex in node_map[node]:
                if not visit[vertex]:
                    visit[vertex] = True
                    dfs(vertex)
        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res+=1
        return res
        