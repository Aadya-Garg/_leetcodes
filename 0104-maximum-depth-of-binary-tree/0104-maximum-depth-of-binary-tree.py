# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """
        if root == None:
            return 0
        depth = 0
        #BFS is using queue
        q = deque([root])
        while q:
            temp_len = len(q)
            for i in range(temp_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
            depth += 1
        return depth
"""