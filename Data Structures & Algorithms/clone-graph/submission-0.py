"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        oldtoNew = {}
        oldtoNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in oldtoNew:
                    oldtoNew[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldtoNew[cur].neighbors.append(oldtoNew[neighbor])
        return oldtoNew[node]

        