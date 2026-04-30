# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []
        q = collections.deque([root])

        while q:
            q_len = len(q)
            right_view = None

            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_view = node
                    q.append(node.left)
                    q.append(node.right)
            if right_view:
                result.append(right_view.val)
        return result


        