# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def updateSums(sum1, sum2, targetSum, res):
    #     val = self.val
    #     # there are always two possible sums
    #     # one follows as: parent's val + curr, other: curr
    #     sum1 += node.val
    #     if sum1 > targetSum:
    #         sum1 = node.val
    #     if sum1 == targetSum:
    #         res += 1
    #         sum1 = node.val
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # print(root, targetSum)
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
            node, sums = stack.pop()
            sum_new = copy.deepcopy(sums)
            # append the look up vals to sums
            curr_val = node.val
            for i in range(len(sum_new)): #sums = [-2] [-5, 11] [6, 0]
                if curr_val == sum_new[i]: # 10 != 8
                    res += 1
                sum_new[i] -= curr_val
            if curr_val == targetSum:
                res += 1
            sum_new.append(targetSum - curr_val) #yes it can be 0 that I am looking for

            if node.right:
                stack.append((node.right, sum_new))

            if node.left:
                stack.append((node.left, sum_new))
        return res
    