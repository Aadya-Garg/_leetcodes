# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # will need to touch all nodes once
        res = float('-inf')
        res_level = 1
        level = 1
        q = deque([root])
        temp_sum = 0
        while q:
            temp = len(q)
            for i in range(temp):
                node = q.popleft()
                temp_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if temp_sum > res:
                res_level = level
                res = temp_sum
            level += 1
            temp_sum = 0
        return res_level

            
        