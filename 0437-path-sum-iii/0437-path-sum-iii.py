# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        stack = [(root, [])]
        res = 0

        while stack:
            node, prevSums = stack.pop()
            sum_new = []
                
            for num in prevSums:
                sum_new.append(num - node.val)
                if num == node.val:
                    res += 1
            diff = targetSum - node.val
            sum_new.append(diff)
            if diff == 0:
                res += 1

            if node.right:
                stack.append((node.right, sum_new))

            if node.left:
                stack.append((node.left, sum_new))
            del(sum_new)
        return res
    