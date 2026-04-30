# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        queue = deque()
        queue.append(root)
        result = 0
        max_heap = []

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                heapq.heappush(max_heap, -node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            while len(max_heap) > k:
                heapq.heappop(max_heap)

        return heapq.heappop(max_heap) * -1
        