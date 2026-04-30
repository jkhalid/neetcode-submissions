# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
        if not subRoot:
            return True
        if not root and not subRoot:
            return True
        
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode])-> bool:

        if not p and not q:
            return True

        queue = deque()
        queue.append((p,q))

        while queue:
            nodep, nodeq = queue.popleft()

            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False
            
            queue.append((nodep.left, nodeq.left))
            queue.append((nodep.right, nodeq.right))
        return True

        
        