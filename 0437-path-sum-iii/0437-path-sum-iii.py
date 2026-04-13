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
        stack = []
        res = 0
        if root.val == targetSum:
            res = 1
        if root.right:
             stack.append((root.right, [targetSum - root.val]))
        if root.left:
            stack.append((root.left, [targetSum - root.val]))

        while stack:
            node, s = stack.pop()
            sum_new = [0]*len(s)
            # append the look up vals to sums
            curr_val = node.val
                
            for i in range(len(s)):
                sum_new[i] = s[i] - curr_val
                if sum_new[i] == 0:
                    res += 1
            
            sum_new.append(targetSum - curr_val) #yes it can be 0 that I am looking for
            if sum_new[-1] == 0:
                res += 1

            if node.right:
                stack.append((node.right, sum_new))

            if node.left:
                stack.append((node.left, sum_new))
            del(sum_new)
        return res
    