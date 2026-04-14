# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # ------ 0 = move left, 1 = move right -------
        if not root:
            return 0
        res = 0
        stack = []
        # (node, dir, res)
        if root.right:
            stack.append((root.right, 0, 1))
        if root.left:
            stack.append((root.left, 1, 1))
        while stack:
            node, dir_, resSoFar = stack.pop()
            if not node:
                continue
            res = max(res, resSoFar)
            if dir_ == 1:
                stack.append((node.right, 0, resSoFar + 1))  
                stack.append((node.left, 1, 1))
            else:
                stack.append((node.left, 1, resSoFar + 1))
                stack.append((node.right, 0, 1))

        return res

    #     resLeft = 0
    #     if not root:
    #         return resLeft
    #     stack = [(root, 0)]
    #     while stack:
    #         node, dir_ = stack.pop()
    #         resLeft += 1
    #         if dir_ == 0 and node.left:
    #             stack.append((node.left, 1))
    #         elif dir_ == 1 and node.right:
    #             stack.append((node.right, 0))
    #         else:
    #             break
    # return max(resLeft, 1 + root.right.longestZigZag())
        



