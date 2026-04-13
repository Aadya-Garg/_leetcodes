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
            sum_new = [0]*len(prevSums)
            # append the look up vals to sums
            curr_val = node.val
                
            for i in range(len(prevSums)):
                sum_new[i] = sprevSumsi] - curr_val
                if sum_new[i] == 0:
                    res += 1
            diff = targetSum - curr_val
            sum_new.append(diff) #yes it can be 0 that I am looking for
            if diff == 0:
                res += 1

            if node.right:
                stack.append((node.right, sum_new))

            if node.left:
                stack.append((node.left, sum_new))
            del(sum_new)
        return res
    