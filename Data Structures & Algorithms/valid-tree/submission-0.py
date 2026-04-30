class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        tree_map = {node : [] for node in range(n)}
        for node , edge in edges:
            tree_map[node].append(edge)
            tree_map[edge].append(node)
        
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
            
            visit.add(node)
            for vertex in tree_map[node]:
                if vertex == parent:
                    continue
                if not dfs(vertex, node):
                    return False
            return True
        
        if not dfs(0,-1):
            return False
        return len(visit) == n
        